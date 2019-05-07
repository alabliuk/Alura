using System;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Threading.Tasks;
using Alura.ListaLeitura.Seguranca;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;

namespace Alura.WebAPI.WebApp.Api
{
    [ApiController]
    [Route("api/[controller]")]
    public class LoginController : Controller
    {
        private readonly SignInManager<Usuario> _signInManager;

        public LoginController(SignInManager<Usuario> signInManager)
        {
            _signInManager = signInManager;
        }

        [HttpPost]
        public async Task<IActionResult> Token(LoginModel model)
        {
            if (ModelState.IsValid)
            {
                var result = await _signInManager.PasswordSignInAsync(model.Login, model.Password, true, true);
                if (result.Succeeded)
                {
                    //cria token (header + payload(claims|Direitos) + signature)

                    var direitos = new[]
                    {
                        new Claim(JwtRegisteredClaimNames.Sub, model.Login),
                        new Claim(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString())
                    };

                    var chave = new SymmetricSecurityKey(System.Text.Encoding.UTF8.GetBytes("chave-de-autenticacao"));
                    var credenciais = new SigningCredentials(chave, SecurityAlgorithms.HmacSha256);

                    var token = new JwtSecurityToken(
                        issuer: "Alura.Web.App",
                        audience: "Postman",
                        claims: direitos,
                        signingCredentials: credenciais,
                        expires: DateTime.Now.AddMinutes(30)
                    );

                    var tokenString = new JwtSecurityTokenHandler().WriteToken(token);
                    return Ok(tokenString);
                }
                return Unauthorized();
            }

            return BadRequest();
        }
    }
}
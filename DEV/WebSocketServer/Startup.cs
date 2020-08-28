using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using System.Net.WebSockets;

namespace WebSocketServer
{
    public class Startup
    {
        
        public void ConfigureServices(IServiceCollection services)
        {
        }

        [Obsolete]
        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            app.UseWebSockets();

            app.Use(async (context, next) =>{

                    if (context.WebSockets.IsWebSocketRequest){

                        WebSocket webSocket = await context.WebSockets.AcceptWebSocketAsync();
                        Console.WriteLine("WebSocket Connected");
                    }
                    else
                    {
                        //Add a Console.WriteLine to see when we move to next Delegate
                        Console.WriteLine("Hello from 2nd Request Delegate - No WebSocket");
                        await next();
                    }   
            });
        
                //New Request Delegate
                app.Run(async context => {
                    Console.WriteLine("Hello from 3rd (terminal) Request Delegate");
                    await context.Response.WriteAsync("Hello from 3rd (terminal) Request Delegate");
                });

                
        
        }

        [Obsolete]
        public void WriteRequestParam(HttpContext context, IHostingEnvironment env){
                
                if (env.IsDevelopment())
                {

                    Console.WriteLine("Request Method: " + context.Request.Method);
                    Console.WriteLine("Request Protocol: " + context.Request.Protocol);

                if (context.Request.Headers != null)
                {

                    Console.WriteLine("Request Headers: ");
                    foreach (var h in context.Request.Headers)
                    {
                       Console.WriteLine("--> " + h.Key + ": " + h.Value);
                    }
                }  
            }
        }
    }
}
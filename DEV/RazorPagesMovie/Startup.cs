using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using System.Net.WebSockets;

namespace RazorPagesMovie
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

            app.Use(async (context, next) =>
                {
                if (context.WebSockets.IsWebSocketRequest)
        {
            WebSocket webSocket = await context.WebSockets.AcceptWebSocketAsync();
            Console.WriteLine("WebSocket Connected");
        }
        else
        {
        await next();
        }
                });
            }
        }
}
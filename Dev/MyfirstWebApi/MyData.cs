using System;

namespace MyfirstWebApi
{
    public class MyDataController
    {
        public DateTime Date { get; set; }

        public int TemperatureC { get; set; }

        public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);

        public string Summary { get; set; }

        public double PiValue {get; set; }

        public string Mood {get; set; }

    }
}

using System.Collections.Generic;
using System.IO;

namespace Generator
{
    internal class Program
    {
        static void Main()
        {
            var path = @"D:\Git\Novel_URFU\Main build\Novel_URFU_22\game\scripts\Arrays";
            var origin = path + @"\GrumblingPhrases.txt";
            GeneratePythonArray(path, "GrumblingArray", origin);
        }

        static void GeneratePythonArray(string path, string arrayname, string originPath)
        {
            string FullNewPath = (path + @"\" + arrayname + ".rpy");
            var values = File.ReadAllLines(originPath);
            if (!File.Exists(FullNewPath))
            {
                File.Create(FullNewPath);
            }
            var lines = new List<string>();
            lines.Add("define " + arrayname + " = [] \nlabel generate_" + arrayname + ":");
            foreach (var i in values)
            {
                lines.Add("    $" + arrayname + ".append(\'" + i + "\')");
            }
            File.WriteAllLines(FullNewPath, lines.ToArray());
        }
    }
}

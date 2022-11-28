using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Windows.Forms;

namespace ArrayRPYCompiler_forms
{
    public partial class Form1 : Form
    {
        bool PathSet = false, dimSet = false;
        public Form1()
        {
            InitializeComponent();

            openFileDialog1.Filter = "Text files|*.txt";
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void tableLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (PathSet & dimSet)
            {
                ArrayTextBox.Text = ArrayTextBox.Text.Replace(" ", "_");
                switch (DimComoBox.SelectedIndex)
                {
                    case 0:
                        GeneratePythonArray(GetFilePath(), ArrayTextBox.Text, openFileDialog1.FileName);
                        break;
                    case 1:
                        GenerateTwoDimPythonArray(GetFilePath(), ArrayTextBox.Text, openFileDialog1.FileName);
                        break;
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (!(openFileDialog1.ShowDialog() == DialogResult.Cancel))
            {
                PathSet = true;
                PathLabel.Text = openFileDialog1.FileName;
                ContentContainer.Items.Clear();
                foreach(var i in File.ReadAllLines(openFileDialog1.FileName))
                {
                    ContentContainer.Items.Add(i);
                }
            }
        }

        void GeneratePythonArray(string path, string arrayname, string originPath)
        {
            string FullNewPath = (path + arrayname + ".rpy");
            var values = File.ReadAllLines(originPath);
            var lines = new List<string>();
            lines.Add("define " + arrayname + " = [] \nlabel generate_" + arrayname + ":");
            foreach (var i in values)
            {
                lines.Add("    $" + arrayname + ".append(\'" + i + "\')");
            }
            File.WriteAllLines(FullNewPath, lines.ToArray());
        }


        void GenerateTwoDimPythonArray(string path, string arrayname, string originPath)
        {
            string FullNewPath = (path + arrayname + ".rpy");
            var values = File.ReadAllLines(originPath);
            var lines = new List<string>();
            lines.Add("define " + arrayname + " = [] \nlabel generate_" + arrayname + ":");
            foreach (var i in values)
            {
                var parts = i.Split(SplitterTB.Text[0]);
                try
                {
                    lines.Add("    $" + arrayname + ".append(['" + parts[0] + "', '" + parts[1] + "'])");
                }
                catch
                {
                    continue;
                }
            }
            File.WriteAllLines(FullNewPath, lines.ToArray());
        }
        string GetFilePath()
        {
            var partArray = openFileDialog1.FileName.Split('\\');
            StringBuilder builder = new StringBuilder();
            for (int i = 0; i < partArray.Length - 1; i++)
            {
                builder.Append(partArray[i]);
                builder.Append('\\');
            }
            return builder.ToString();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

            dimSet = true;
            if (DimComoBox.SelectedItem == DimComoBox.Items[1])
            {
                SplitterTB.Enabled = true;
            }
            else SplitterTB.Enabled = false;
        }
    }
}

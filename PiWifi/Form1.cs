using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
 
namespace PiWifi
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public List<string> GetWifiList()
        {
            string args = ("");
            var prc = new System.Diagnostics.Process();

            prc.StartInfo = new System.Diagnostics.ProcessStartInfo()
            {
                FileName = "netsh",
                Arguments = "wlan show all",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                CreateNoWindow=true
            };

            prc.Start();
           return prc.StandardOutput.ReadToEnd().Split(Environment.NewLine.ToCharArray()).ToList().Where(p => p.Trim().ToLower().StartsWith("ssid")&& p.Contains(":")).Select(p=>p.Split(':')[1].Trim().Replace("\"","")).ToList();
            
        }
        void ScanWifi()
        {
            listBox1.DataSource = GetWifiList();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string wifiFile = System.IO.Path.Combine(Application.StartupPath, "wpa_supplicant.conf");
            string wifiTemp = System.IO.Path.Combine(Application.StartupPath, "witemp.txt");

            var msg = System.IO.File.ReadAllText(wifiTemp).Replace("@ssid", NetWrokNametextBox.Text).Replace("@pwd", PwdtextBox.Text);System.IO.File.WriteAllText(wifiFile, msg, System.Text.Encoding.UTF8);
            MessageBox.Show("Wifi data has been written to PI");
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ScanWifi();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            ScanWifi();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex>-1)
            {
                NetWrokNametextBox.Text = listBox1.Items[listBox1.SelectedIndex].ToString();
            }
           
        }
    }
}

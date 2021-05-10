using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Http;
using System.Net;
using CsvHelper;
using System.IO;

namespace G22App1
{
   

    public partial class FormApp : Form
    {

        private static readonly HttpClient client = new HttpClient();

        public FormApp()
        {
            InitializeComponent();
        }

       

        private void Form1_Load(object sender, EventArgs e)
        {
            PnlMainMenu.Visible = true;
            PnlMainMenu.BringToFront();
        }

        private async void BtnMainListenToMusic_Click(object sender, EventArgs e)
        {
            

            OpenFileDialog openFileDialog1 = new OpenFileDialog
            {
                InitialDirectory = @"C:\",
                Title = "Browse Music Files",

                CheckFileExists = true,
                CheckPathExists = true,

                DefaultExt = "ogg",
                Filter = "ogg files (*.ogg)|*.ogg",
                FilterIndex = 2,
                RestoreDirectory = true,

                ReadOnlyChecked = true,
                ShowReadOnly = true
            };

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {

                try
                {
                   
                    //  using var client = new HttpClient();

                    //var values = ;

                    //  var content = new FormUrlEncodedContent(values);

                    //var response = await client.PostAsync("", content);

                    // var responseString = await response.Content.ReadAsStringAsync();

                    try
                    {
                        WebClient client = new WebClient();
                        string myFile = openFileDialog1.FileName;
                        client.Credentials = CredentialCache.DefaultCredentials;
                        client.UploadFile(@"http://104.154.97.229:5000/analyseSong", "POST", myFile);
                        client.Dispose();

                        PnlMainMenu.Visible = false;
                        PnlListening.Visible = true;
                        PnlListening.BringToFront();
                    }
                    catch (Exception err)
                    {
                        MessageBox.Show(err.Message);
                    }

                   
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Security error.\n\nError message: {ex.Message}\n\n" +
                    $"Details:\n\n{ex.StackTrace}");

                }





            }
            else
            {
                MessageBox.Show("Either no file was selected or the file could not be used, please try again!");
            }
           
        }

       

        private void BtnListeningBack_Click(object sender, EventArgs e)
        {
            PnlListening.Visible = false;
            PnlMainMenu.Visible = true;
            PnlMainMenu.BringToFront();
        }

        private void BtnListeningFoundHelp_Click(object sender, EventArgs e)
        {
            MessageBox.Show("The algorithm has returned with the result it has deduced. You can choose to add this to teh records by clicking the 'Add to Data' button, or you can expunge it and go back to the main menu by clicking the 'Go Back' button.");
        }

      
       
        private void LblListening_Click(object sender, EventArgs e)
        {
            PnlListening.Visible = false;
            PnlListeningFound.Visible = true;
            PnlListeningFound.BringToFront();
        }

        private void BtnMainTheAlgorithmsDeductions_Click(object sender, EventArgs e)
        {
            PnlMainMenu.Visible = false;
            PnlDeductions.Visible = true;
            PnlDeductions.BringToFront();

            using (var reader = new StreamReader("deductions.csv"))
            using (var csv = new CsvReader((IParser)reader))
            {
                var records = csv.GetRecords<csvFunctions>();

                for (int x = 0; x == records.Count()-1; x ++)
                {
                    LstDeductions.Items.Add(records.ElementAt(x));
                }
            }

        }

        private void BtnDeductionsBack_Click(object sender, EventArgs e)
        {
            PnlDeductions.Visible = false;
            PnlMainMenu.Visible = true;
            PnlMainMenu.BringToFront();
        }

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {
            //this is where the file would be passed onto the backend
        }

        private void BtnListeningBack_Click_1(object sender, EventArgs e)
        {
            PnlListening.Visible = false;
            PnlMainMenu.Visible = true;
            PnlMainMenu.BringToFront();
        }

        private void BtnListeningFoundBack_Click(object sender, EventArgs e)
        {
            PnlListeningFound.Visible = false;
            PnlMainMenu.Visible = true;
            PnlMainMenu.BringToFront();
        }

        private void BtnFoundAdd_Click(object sender, EventArgs e)
        {

        }

        private void BtnMainSettings_Click(object sender, EventArgs e)
        {
            MessageBox.Show("This is the main menu, from here you can either go to the 'Add Music' section fo the program to upload a .ogg music file to be sorted between classical or rock, or you can check to see previous entries in the 'Algorithm's Deductions'.");
        }

        private void BtnListeningSettings_Click(object sender, EventArgs e)
        {
            MessageBox.Show("The program is checking your music and once it is finished, you will be shown the result! You could back out using the 'Go Back' button if you dont wish to test that music file any more.");
        }

        private void BtnDeductionsHelp_Click(object sender, EventArgs e)
        {
            MessageBox.Show("This is the results or deductions screen. This shows the previous results from the algorithm, you can go back to the main menu by clicking the 'Main Menu' button.");
        }

        public class csvFunctions
        {
            public string Name { get; set; }
            public string Classification { get; set; }
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}

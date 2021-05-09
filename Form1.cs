using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace G22App1
{
    public partial class FormApp : Form
    {
        public FormApp()
        {
            InitializeComponent();
        }

       

        private void Form1_Load(object sender, EventArgs e)
        {
            PnlMainMenu.Visible = true;
            PnlMainMenu.BringToFront();
        }

        private void BtnMainListenToMusic_Click(object sender, EventArgs e)
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

            openFileDialog1.ShowDialog();
            
            PnlMainMenu.Visible = false;
            PnlListening.Visible = true;
            PnlListening.BringToFront();
        }

       

        private void BtnListeningBack_Click(object sender, EventArgs e)
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

        private void ListeningFoundBack_Click(object sender, EventArgs e)
        {
            PnlListeningFound.Visible = false;
            PnlMainMenu.Visible = true;
            PnlMainMenu.BringToFront();
        }

    }
}

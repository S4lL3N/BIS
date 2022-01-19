namespace SQLGenerator
{
    public partial class Form1 : Form
    {
        Boolean instnum = false;
        Boolean batchnum = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            instnum = checkBox1.Checked;

        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            batchnum = checkBox2.Checked;


        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }


        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = GenerateStatement();


        }
        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                button1.PerformClick();
            }
        }
        //clear button
        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            checkBox1.Checked = false;
            checkBox2.Checked = false;
            comboBox1.Text = "";
            richTextBox1.Text = "";
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }
        private String GenerateStatement()
        {
            String query;
            String key;
            String output;

            query = comboBox1.Text;
            key = textBox1.Text;

            if (query.Equals("Transactions") && instnum)
            {
                output = TransactionsInstnum(key);
                //saves to clipboard
                Clipboard.SetText(output);
                return output;
            }
            else if (query.Equals("Transactions") && batchnum)
            {

                output = TransactionsBatchNum(key);
                //saves to clipboard
                Clipboard.SetText(output);
                return output;
            }
            else if (query.Equals("EFile") && instnum)
            {
                output = EfileInstNum(key);
                Clipboard.SetText(output);
                return output;
            }
            else if (query.Equals("EFile") && batchnum)
            {
                output = EfileBatchNum(key);
                Clipboard.SetText(output);
                return output;
            }
            else if (query.Equals("EFile via Tracking Num."))
            {
                output = EfileTrackingNumber(key);
                Clipboard.SetText(output);
                return output;
            }
            else if (query.Equals("Image Details"))
            {
                checkBox1.Checked = true;
                output = ImageDetails(key);
                Clipboard.SetText(output);
                return output;
            }
            else if (query.Equals("Change Password"))
            {
                output = Password(key);
                Clipboard.SetText(output);
                return output;
            }
            else if (query.Equals("Master Settings"))
            {
                output = MasterSettings();
                Clipboard.SetText(output);
                return output;
            }
            else if (query.Equals("Printer and Term Setup"))
            {
                output = PrinterAndTerminalSettings(key);
                Clipboard.SetText(output);
                return output;
            }
            else
            {
                return " ";
            }
        }

        private String TransactionsInstnum(String key)
        {
            String output;
            output = "SELECT * FROM TBL_Transactions WHERE InstNum = '" + key + "';";
            output += "\nSELECT * FROM TBL_CashJournal WHERE InstNum = '" + key + "';";
            output += "\nSELECT * FROM TBL_CJMoney WHERE BatchNum = ' ';";
            output += "\nSELECT * FROM TBL_ARtrans WHERE BatchNum = ' ';";
            return output;
        }
        private String TransactionsBatchNum(String key)
        {
            String output;
            output = "SELECT * FROM TBL_Transactions WHERE BatchNum = '" + key + "';";
            output += "\nSELECT * FROM TBL_CashJournal WHERE BatchNum = '" + key + "';";
            output += "\nSELECT * FROM TBL_CJMoney WHERE BatchNum = '" + key + "';";
            output += "\nSELECT * FROM TBL_ARtrans WHERE BatchNum = '" + key + "';";
            return output;
        }
        private String EfileInstNum(String key)
        {
            String output;
            output = "SELECT* FROM TBL_TransEfile WHERE InstNum = '" + key + "';";
            output += "\nSELECT* FROM EFL_Trans WHERE InstNum = '" + key + "';";
            output += "\nSELECT* FROM EFL_EfileLog WHERE InstNum = '" + key + "';";
            return output;
        }
        private String EfileBatchNum(String key)
        {
            String output;
            output = "SELECT* FROM TBL_TransEfile WHERE MosBatchNum = '" + key + "';";
            output += "\nSELECT* FROM EFL_Trans WHERE BatchNum = '" + key + "';";
            output += "\nSELECT* FROM EFL_EfileLog WHERE BatchNum = '" + key + "';";
            return output;
        }
        private String EfileTrackingNumber(String key)
        {
            String output;
            output = "select te.InstNum,te.BatchNum,t.InstNum,t.BatchNum,t.Status,e.code,tb.ReceivedFrom,t.TrackingNumber,Tran1.BookNum,Tran1.BPageNum,Tran1.ImgID";
            output += "\nfrom EFL_Trans t";
            output += "\njoin EFL_EfileLog e on t.InstNum = e.InstNum";
            output += "\njoinjoin EFL_TransBatchInfo tb on t.BatchNum = tb.BatchNum";
            output += "\njoinjoin TBL_TransEfile te on t.InstNum = te.MosInstNum";
            output += "\njoinjoin TBL_Transactions Tran1 on te.InstNum = Tran1.InstNum";
            output += "\njoinwhere t. TrackingNumber = '" + key + "'";
            output += "\njoinand e.Code IN(Select Code From EFL_EfileLog where t.InstNum order by ID)";
            output += "\njoinOrder by t.BatchNum;";

            return output;
        }
        private String ImageDetails(String key)
        {
            String output;
            output = "SELECT * FROM TBL_Transactions WHERE InstNum = '" + key + "';";
            output += "\nSELECT * FROM IMG_ImageDetails WHERE ImgID = '';";

            return output;
        }
        private String Password(String key)
        {
            String output;
            output = "SELECT * FROM TBL_Users;";
            output += "\nSELECT * FROM TBL_Users WHERE Fullname LIKE = '%" + key + "%'";
            return output;
        }

        private String MasterSettings()
        {
            String output;
            output = "SELECT * FROM TBL_MasterSettings;";
            return output;

        }

        private String PrinterAndTerminalSettings(String key)
        {
            String output;
            output = "SELECT * FROM TBL_Printersetup;";
            output += "\nSELECT * FROM TBL_Terminalsetup;";
            output += "\nSELECT * FROM TBL_Terminalsetup WHERE TermNum ='"+ key +"';";
            return output;
        }

    }
}
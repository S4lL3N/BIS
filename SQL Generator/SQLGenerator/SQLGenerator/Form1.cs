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
            textBox1.Text = "";
            checkBox1.Checked = false;
            checkBox2.Checked = false;
            comboBox1.Text = "";

        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }
        private String GenerateStatement()
        {
            String table;
            String key;
            String output;

            table = comboBox1.Text;
            key = textBox1.Text;

            if (table.Equals("Transactions") && instnum)
            {
                output = "SELECT * FROM TBL_Transactions WHERE InstNum = '" + key + "';";
                output += "\nSELECT * FROM TBL_CashJournal WHERE InstNum = '" + key + "';";
                output += "\nSELECT * FROM TBL_CJMoney WHERE BatchNum = ' ';";
                output += "\nSELECT * FROM TBL_ARtrans WHERE BatchNum = ' ';";

                //saves to clipboard
                Clipboard.SetText(output);

                return output;
            }
            else if (table.Equals("Transactions") && batchnum)
            {
                output = "SELECT * FROM TBL_Transactions WHERE BatchNum = '" + key + "';";
                output += "\nSELECT * FROM TBL_CashJournal WHERE BatchNum = '" + key + "';";
                output += "\nSELECT * FROM TBL_CJMoney WHERE BatchNum = '" + key + "';";
                output += "\nSELECT * FROM TBL_ARtrans WHERE BatchNum = '" + key + "';";

                //saves to clipboard
                Clipboard.SetText(output);

                return output;
            }
            else
            {
                return " ";
            }
        }
    }
}
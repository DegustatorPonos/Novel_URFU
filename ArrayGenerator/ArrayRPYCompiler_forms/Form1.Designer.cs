namespace ArrayRPYCompiler_forms
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.ArrayTextBox = new System.Windows.Forms.TextBox();
            this.GenerateButton = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.ChooseButton = new System.Windows.Forms.Button();
            this.PathLabel = new System.Windows.Forms.Label();
            this.ContentContainer = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // ArrayTextBox
            // 
            this.ArrayTextBox.Location = new System.Drawing.Point(12, 529);
            this.ArrayTextBox.Name = "ArrayTextBox";
            this.ArrayTextBox.Size = new System.Drawing.Size(166, 20);
            this.ArrayTextBox.TabIndex = 1;
            this.ArrayTextBox.Text = "Array name";
            this.ArrayTextBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // GenerateButton
            // 
            this.GenerateButton.Location = new System.Drawing.Point(851, 526);
            this.GenerateButton.Name = "GenerateButton";
            this.GenerateButton.Size = new System.Drawing.Size(148, 23);
            this.GenerateButton.TabIndex = 1;
            this.GenerateButton.Text = "Generate";
            this.GenerateButton.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;
            this.GenerateButton.UseVisualStyleBackColor = true;
            this.GenerateButton.Click += new System.EventHandler(this.button1_Click);
            // 
            // ChooseButton
            // 
            this.ChooseButton.Location = new System.Drawing.Point(184, 527);
            this.ChooseButton.Name = "ChooseButton";
            this.ChooseButton.Size = new System.Drawing.Size(68, 23);
            this.ChooseButton.TabIndex = 4;
            this.ChooseButton.Text = "Choose file";
            this.ChooseButton.UseVisualStyleBackColor = true;
            this.ChooseButton.Click += new System.EventHandler(this.button2_Click);
            // 
            // PathLabel
            // 
            this.PathLabel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.PathLabel.Location = new System.Drawing.Point(258, 526);
            this.PathLabel.Name = "PathLabel";
            this.PathLabel.Size = new System.Drawing.Size(587, 23);
            this.PathLabel.TabIndex = 7;
            this.PathLabel.Text = "Path";
            this.PathLabel.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // ContentContainer
            // 
            this.ContentContainer.FormattingEnabled = true;
            this.ContentContainer.Location = new System.Drawing.Point(12, 12);
            this.ContentContainer.Name = "ContentContainer";
            this.ContentContainer.Size = new System.Drawing.Size(987, 498);
            this.ContentContainer.TabIndex = 8;
            this.ContentContainer.SelectedIndexChanged += new System.EventHandler(this.ContentContainer_SelectedIndexChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSize = true;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ClientSize = new System.Drawing.Size(1005, 555);
            this.Controls.Add(this.ContentContainer);
            this.Controls.Add(this.PathLabel);
            this.Controls.Add(this.ChooseButton);
            this.Controls.Add(this.ArrayTextBox);
            this.Controls.Add(this.GenerateButton);
            this.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.Name = "Form1";
            this.Text = "RPY array compiler";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.TextBox ArrayTextBox;
        private System.Windows.Forms.Button GenerateButton;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button ChooseButton;
        private System.Windows.Forms.Label PathLabel;
        private System.Windows.Forms.ListBox ContentContainer;
    }
}


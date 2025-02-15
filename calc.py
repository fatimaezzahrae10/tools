from ttkbootstrap import ttk
import tkinter as tk
import math

class CalculatorApp:
    """A calculator application with basic arithmetic operations"""
    
    def __init__(self, root):
        self.root = root
        self.current_expression = ""
        self.last_result = None
        self.setup_ui()

    def setup_ui(self):
        """Setup the calculator interface"""
        self.root.title("Calculator")
        self.root.geometry("400x500")
        
        # Configure the grid
        for i in range(7):  # Increased rows for better spacing
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        # Display
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            state="readonly"
        )
        self.display.grid(
            row=0, 
            column=0, 
            columnspan=4, 
            padx=10, 
            pady=20, 
            sticky="nsew"
        )

        # Calculator buttons configuration
        self.create_buttons()

        # Bind keyboard events
        self.setup_keyboard_bindings()

    def create_buttons(self):
        """Create and configure all calculator buttons"""
        buttons = [
            ('C', 1, 0, 'secondary'), ('±', 1, 1, 'secondary'),
            ('%', 1, 2, 'secondary'), ('/', 1, 3, 'warning'),
            ('7', 2, 0, 'default'), ('8', 2, 1, 'default'),
            ('9', 2, 2, 'default'), ('*', 2, 3, 'warning'),
            ('4', 3, 0, 'default'), ('5', 3, 1, 'default'),
            ('6', 3, 2, 'default'), ('-', 3, 3, 'warning'),
            ('1', 4, 0, 'default'), ('2', 4, 1, 'default'),
            ('3', 4, 2, 'default'), ('+', 4, 3, 'warning'),
            ('0', 5, 0, 'default'), ('.', 5, 1, 'default'),
            ('=', 5, 2, 'success', 2)  # span 2 columns
        ]

        for button in buttons:
            if len(button) == 5:  # Button with column span
                text, row, col, style, colspan = button
                ttk.Button(
                    self.root,
                    text=text,
                    style=f"{style}.TButton",
                    command=lambda t=text: self.on_button_click(t)
                ).grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")
            else:
                text, row, col, style = button
                ttk.Button(
                    self.root,
                    text=text,
                    style=f"{style}.TButton",
                    command=lambda t=text: self.on_button_click(t)
                ).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

    def setup_keyboard_bindings(self):
        """Setup keyboard bindings for calculator operations"""
        self.root.bind('<Return>', lambda e: self.on_button_click('='))
        self.root.bind('<BackSpace>', lambda e: self.on_button_click('C'))
        self.root.bind('<Escape>', lambda e: self.clear_expression())
        
        # Number keys
        for i in range(10):
            self.root.bind(str(i), lambda e, i=i: self.on_button_click(str(i)))
        
        # Operation keys
        self.root.bind('+', lambda e: self.on_button_click('+'))
        self.root.bind('-', lambda e: self.on_button_click('-'))
        self.root.bind('*', lambda e: self.on_button_click('*'))
        self.root.bind('/', lambda e: self.on_button_click('/'))
        self.root.bind('.', lambda e: self.on_button_click('.'))

    def on_button_click(self, button_text):
        """Handle calculator button clicks"""
        if button_text == '=':
            self.evaluate_expression()
        elif button_text == 'C':
            self.clear_expression()
        elif button_text == '±':
            self.toggle_sign()
        elif button_text == '%':
            self.calculate_percentage()
        else:
            self.add_to_expression(button_text)

    def add_to_expression(self, value):
        """Add a value to the current expression"""
        if value in '+-*/' and self.current_expression and self.current_expression[-1] in '+-*/':
            self.current_expression = self.current_expression[:-1] + value
        else:
            self.current_expression += value
        self.display_var.set(self.current_expression)

    def evaluate_expression(self):
        """Evaluate the current mathematical expression"""
        try:
            if self.current_expression:
                result = eval(self.current_expression)
                self.last_result = result
                self.display_var.set(f"{result:g}" if abs(result) < 1e10 else f"{result:.10e}")
                self.current_expression = str(result)
        except Exception:
            self.display_var.set("Error")
            self.current_expression = ""

    def clear_expression(self):
        """Clear the current expression"""
        self.current_expression = ""
        self.display_var.set("")

    def toggle_sign(self):
        """Toggle the sign of the current number"""
        try:
            if self.current_expression:
                if self.current_expression.startswith('-'):
                    self.current_expression = self.current_expression[1:]
                else:
                    self.current_expression = '-' + self.current_expression
                self.display_var.set(self.current_expression)
        except Exception:
            self.display_var.set("Error")
            self.current_expression = ""

    def calculate_percentage(self):
        """Calculate percentage of the current number"""
        try:
            if self.current_expression:
                result = eval(self.current_expression) / 100
                self.current_expression = str(result)
                self.display_var.set(self.current_expression)
        except Exception:
            self.display_var.set("Error")
            self.current_expression = ""

def main():
    """Run the calculator as a standalone application"""
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

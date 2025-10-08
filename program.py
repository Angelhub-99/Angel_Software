import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os


class ModernMultiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Multi-Purpose Application")
        self.root.geometry("900x700")
        self.root.config(bg="#1a1a2e")
        
        # Data file for contacts
        self.data_file = "contacts.json"
        self.contacts = self.load_contacts()
        
        # Configure modern styles
        self.configure_styles()
        
        # Create Header
        self.create_header()
        
        # Create Notebook (Tabbed Interface)
        self.notebook = ttk.Notebook(self.root, style='Modern.TNotebook')
        self.notebook.pack(expand=True, fill='both', padx=15, pady=(0, 15))
        
        # Create All Tabs
        self.create_contact_manager_tab()
        self.create_unit_converter_tab()
        self.create_age_calculator_tab()
        self.create_bmi_calculator_tab()
    
    def configure_styles(self):
        """Configure modern ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Notebook style
        style.configure('Modern.TNotebook', background='#16213e', borderwidth=0)
        style.configure('Modern.TNotebook.Tab', 
                       background='#0f3460',
                       foreground='#ffffff',
                       padding=[20, 10],
                       font=('Arial', 10, 'bold'))
        style.map('Modern.TNotebook.Tab',
                 background=[('selected', '#e94560')],
                 foreground=[('selected', '#ffffff')])
        
        # Combobox style
        style.configure('Modern.TCombobox',
                       fieldbackground='#ffffff',
                       background='#e94560',
                       foreground='#16213e',
                       arrowcolor='#ffffff',
                       borderwidth=0)
    
    def create_header(self):
        """Create modern gradient-like header"""
        header_frame = tk.Frame(self.root, bg='#e94560', height=100)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Title with modern font
        title = tk.Label(
            header_frame,
            text="🚀 Modern Multi-Purpose App",
            font=('Helvetica', 28, 'bold'),
            bg='#e94560',
            fg='#ffffff'
        )
        title.pack(pady=20)
        
        # Subtitle
        subtitle = tk.Label(
            header_frame,
            text="Contacts • Converters • Calculators • All in One Place",
            font=('Arial', 11),
            bg='#e94560',
            fg='#ffffff'
        )
        subtitle.pack()
    
    def create_modern_button(self, parent, text, command, bg_color, width=20):
        """Create a modern styled button with hover effect"""
        button = tk.Button(
            parent,
            text=text,
            font=('Arial', 11, 'bold'),
            bg=bg_color,
            fg='#ffffff',
            activebackground=self.darken_color(bg_color),
            activeforeground='#ffffff',
            bd=0,
            padx=20,
            pady=12,
            cursor='hand2',
            relief=tk.FLAT,
            width=width,
            command=command
        )
        
        # Hover effects
        button.bind('<Enter>', lambda e: button.config(bg=self.lighten_color(bg_color)))
        button.bind('<Leave>', lambda e: button.config(bg=bg_color))
        
        return button
    
    def lighten_color(self, hex_color):
        """Lighten a hex color"""
        # Simple lightening by increasing RGB values
        rgb = self.hex_to_rgb(hex_color)
        lighter = tuple(min(255, int(c * 1.2)) for c in rgb)
        return self.rgb_to_hex(lighter)
    
    def darken_color(self, hex_color):
        """Darken a hex color"""
        rgb = self.hex_to_rgb(hex_color)
        darker = tuple(max(0, int(c * 0.8)) for c in rgb)
        return self.rgb_to_hex(darker)
    
    def hex_to_rgb(self, hex_color):
        """Convert hex to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def rgb_to_hex(self, rgb):
        """Convert RGB to hex"""
        return '#%02x%02x%02x' % rgb
    
    def create_modern_entry(self, parent, width=30):
        """Create modern styled entry"""
        entry = tk.Entry(
            parent,
            font=('Arial', 11),
            bg='#ffffff',
            fg='#16213e',
            insertbackground='#e94560',
            relief=tk.FLAT,
            bd=2,
            highlightthickness=2,
            highlightcolor='#e94560',
            highlightbackground='#d1d1d1',
            width=width
        )
        return entry
    
    # ============================================
    # TAB 1: CONTACT MANAGER
    # ============================================
    def create_contact_manager_tab(self):
        contact_frame = tk.Frame(self.notebook, bg='#f5f5f5')
        self.notebook.add(contact_frame, text='📇  Contact Manager')
        
        # Main container with padding
        main_container = tk.Frame(contact_frame, bg='#f5f5f5')
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left side - Input form
        left_frame = tk.Frame(main_container, bg='#ffffff', relief=tk.FLAT, bd=0)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Form title
        form_title = tk.Label(
            left_frame,
            text='Contact Details',
            font=('Arial', 16, 'bold'),
            bg='#ffffff',
            fg='#16213e'
        )
        form_title.pack(pady=(20, 15))
        
        # Input fields container
        inputs_frame = tk.Frame(left_frame, bg='#ffffff')
        inputs_frame.pack(padx=30, pady=10, fill=tk.BOTH, expand=True)
        
        # Name
        tk.Label(inputs_frame, text='Full Name', font=('Arial', 10, 'bold'), 
                bg='#ffffff', fg='#16213e').grid(row=0, column=0, sticky='w', pady=(10, 5))
        self.name_entry = self.create_modern_entry(inputs_frame, 35)
        self.name_entry.grid(row=1, column=0, pady=(0, 15), ipady=5)
        
        # Phone
        tk.Label(inputs_frame, text='Phone Number', font=('Arial', 10, 'bold'),
                bg='#ffffff', fg='#16213e').grid(row=2, column=0, sticky='w', pady=(10, 5))
        self.phone_entry = self.create_modern_entry(inputs_frame, 35)
        self.phone_entry.grid(row=3, column=0, pady=(0, 15), ipady=5)
        
        # Email
        tk.Label(inputs_frame, text='Email Address', font=('Arial', 10, 'bold'),
                bg='#ffffff', fg='#16213e').grid(row=4, column=0, sticky='w', pady=(10, 5))
        self.email_entry = self.create_modern_entry(inputs_frame, 35)
        self.email_entry.grid(row=5, column=0, pady=(0, 15), ipady=5)
        
        # Address
        tk.Label(inputs_frame, text='Address', font=('Arial', 10, 'bold'),
                bg='#ffffff', fg='#16213e').grid(row=6, column=0, sticky='w', pady=(10, 5))
        self.address_text = tk.Text(
            inputs_frame,
            font=('Arial', 11),
            bg='#ffffff',
            fg='#16213e',
            relief=tk.FLAT,
            bd=2,
            highlightthickness=2,
            highlightcolor='#e94560',
            highlightbackground='#d1d1d1',
            width=35,
            height=4
        )
        self.address_text.grid(row=7, column=0, pady=(0, 15))
        
        # Buttons
        button_frame = tk.Frame(left_frame, bg='#ffffff')
        button_frame.pack(pady=20)
        
        self.create_modern_button(button_frame, '✓ Add Contact', self.add_contact, '#28a745', 12).pack(side=tk.LEFT, padx=5)
        self.create_modern_button(button_frame, '✎ Update', self.update_contact, '#007bff', 10).pack(side=tk.LEFT, padx=5)
        self.create_modern_button(button_frame, '⟲ Clear', self.clear_fields, '#ffc107', 10).pack(side=tk.LEFT, padx=5)
        
        # Right side - Contact list
        right_frame = tk.Frame(main_container, bg='#ffffff', relief=tk.FLAT)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # List title
        list_title = tk.Label(
            right_frame,
            text='Contact List',
            font=('Arial', 16, 'bold'),
            bg='#ffffff',
            fg='#16213e'
        )
        list_title.pack(pady=(20, 10))
        
        # Search
        search_container = tk.Frame(right_frame, bg='#ffffff')
        search_container.pack(fill='x', padx=20, pady=(0, 15))
        
        tk.Label(search_container, text='🔍', font=('Arial', 14), bg='#ffffff').pack(side=tk.LEFT, padx=(0, 5))
        self.search_entry = self.create_modern_entry(search_container, 30)
        self.search_entry.pack(side=tk.LEFT, fill='x', expand=True, ipady=5)
        self.search_entry.bind('<KeyRelease>', lambda e: self.search_contacts())
        
        # Treeview
        tree_container = tk.Frame(right_frame, bg='#ffffff')
        tree_container.pack(fill=tk.BOTH, expand=True, padx=20)
        
        scrollbar = ttk.Scrollbar(tree_container)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        
        self.tree = ttk.Treeview(
            tree_container,
            columns=('Name', 'Phone', 'Email'),
            show='headings',
            yscrollcommand=scrollbar.set,
            height=12
        )
        scrollbar.config(command=self.tree.yview)
        
        self.tree.heading('Name', text='Name')
        self.tree.heading('Phone', text='Phone')
        self.tree.heading('Email', text='Email')
        
        self.tree.column('Name', width=150)
        self.tree.column('Phone', width=120)
        self.tree.column('Email', width=180)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind('<ButtonRelease-1>', self.on_select)
        
        # Delete button
        self.create_modern_button(right_frame, '🗑 Delete Selected', self.delete_contact, '#dc3545', 18).pack(pady=15)
        
        self.refresh_contact_list()
    
    # Contact Manager Methods
    def load_contacts(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_contacts(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.contacts, f, indent=4)
    
    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_text.get('1.0', tk.END).strip()
        
        if not name:
            messagebox.showerror('Error', 'Name is required!')
            return
        
        self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        self.save_contacts()
        self.refresh_contact_list()
        self.clear_fields()
        messagebox.showinfo('Success', 'Contact added successfully! ✓')
    
    def update_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror('Error', 'Please select a contact to update!')
            return
        
        index = self.tree.index(selected[0])
        name = self.name_entry.get().strip()
        
        if not name:
            messagebox.showerror('Error', 'Name is required!')
            return
        
        self.contacts[index] = {
            'name': name,
            'phone': self.phone_entry.get().strip(),
            'email': self.email_entry.get().strip(),
            'address': self.address_text.get('1.0', tk.END).strip()
        }
        
        self.save_contacts()
        self.refresh_contact_list()
        self.clear_fields()
        messagebox.showinfo('Success', 'Contact updated successfully! ✓')
    
    def delete_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror('Error', 'Please select a contact to delete!')
            return
        
        if messagebox.askyesno('Confirm', 'Delete this contact?'):
            index = self.tree.index(selected[0])
            del self.contacts[index]
            self.save_contacts()
            self.refresh_contact_list()
            self.clear_fields()
            messagebox.showinfo('Success', 'Contact deleted! ✓')
    
    def refresh_contact_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for contact in self.contacts:
            self.tree.insert('', tk.END, values=(contact['name'], contact['phone'], contact['email']))
    
    def search_contacts(self):
        search_term = self.search_entry.get().lower()
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for contact in self.contacts:
            if search_term in contact['name'].lower():
                self.tree.insert('', tk.END, values=(contact['name'], contact['phone'], contact['email']))
    
    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            contact = self.contacts[index]
            
            self.clear_fields()
            self.name_entry.insert(0, contact['name'])
            self.phone_entry.insert(0, contact['phone'])
            self.email_entry.insert(0, contact['email'])
            self.address_text.insert('1.0', contact['address'])
    
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_text.delete('1.0', tk.END)
    
    # ============================================
    # TAB 2: UNIT CONVERTER
    # ============================================
    def create_unit_converter_tab(self):
        unit_frame = tk.Frame(self.notebook, bg='#f5f5f5')
        self.notebook.add(unit_frame, text='🔄  Unit Converter')
        
        container = tk.Frame(unit_frame, bg='#ffffff', relief=tk.FLAT)
        container.place(relx=0.5, rely=0.5, anchor='center', width=600, height=500)
        
        # Title with icon
        tk.Label(
            container,
            text='⚡ Unit Converter',
            font=('Arial', 22, 'bold'),
            bg='#ffffff',
            fg='#16213e'
        ).pack(pady=(30, 20))
        
        # Conversion type
        type_frame = tk.Frame(container, bg='#ffffff')
        type_frame.pack(pady=15)
        
        tk.Label(type_frame, text='Conversion Type:', font=('Arial', 12, 'bold'),
                bg='#ffffff', fg='#16213e').pack(side=tk.LEFT, padx=10)
        
        self.conversion_type = ttk.Combobox(
            type_frame,
            values=['Temperature', 'Weight', 'Length'],
            font=('Arial', 11),
            state='readonly',
            width=18,
            style='Modern.TCombobox'
        )
        self.conversion_type.pack(side=tk.LEFT, padx=5)
        self.conversion_type.current(0)
        self.conversion_type.bind('<<ComboboxSelected>>', self.update_unit_options)
        
        # Input frame with modern styling
        input_container = tk.Frame(container, bg='#f8f9fa', relief=tk.FLAT, bd=0)
        input_container.pack(pady=20, padx=40, fill='x')
        
        # Value
        tk.Label(input_container, text='Value:', font=('Arial', 11, 'bold'),
                bg='#f8f9fa', fg='#16213e').pack(anchor='w', pady=(15, 5), padx=20)
        self.unit_value = self.create_modern_entry(input_container, 40)
        self.unit_value.pack(pady=(0, 15), padx=20, ipady=8)
        
        # From
        tk.Label(input_container, text='From:', font=('Arial', 11, 'bold'),
                bg='#f8f9fa', fg='#16213e').pack(anchor='w', pady=(10, 5), padx=20)
        self.from_unit = ttk.Combobox(input_container, font=('Arial', 11),
                                     state='readonly', width=38, style='Modern.TCombobox')
        self.from_unit.pack(pady=(0, 15), padx=20)
        
        # To
        tk.Label(input_container, text='To:', font=('Arial', 11, 'bold'),
                bg='#f8f9fa', fg='#16213e').pack(anchor='w', pady=(10, 5), padx=20)
        self.to_unit = ttk.Combobox(input_container, font=('Arial', 11),
                                    state='readonly', width=38, style='Modern.TCombobox')
        self.to_unit.pack(pady=(0, 15), padx=20)
        
        # Convert button
        self.create_modern_button(container, '🔄 Convert Now', self.convert_units, '#e94560', 20).pack(pady=20)
        
        # Result
        self.unit_result = tk.Label(
            container,
            text='Result will appear here',
            font=('Arial', 13, 'bold'),
            bg='#e8f5e9',
            fg='#2e7d32',
            relief=tk.FLAT,
            bd=0,
            pady=20
        )
        self.unit_result.pack(fill='x', padx=40, pady=(10, 20))
        
        self.update_unit_options()
    
    def update_unit_options(self, event=None):
        conversion_type = self.conversion_type.get()
        
        if conversion_type == 'Temperature':
            units = ['Celsius', 'Fahrenheit', 'Kelvin']
        elif conversion_type == 'Weight':
            units = ['Kilograms', 'Pounds', 'Grams', 'Ounces']
        else:
            units = ['Meters', 'Feet', 'Kilometers', 'Miles', 'Centimeters', 'Inches']
        
        self.from_unit['values'] = units
        self.to_unit['values'] = units
        self.from_unit.current(0)
        self.to_unit.current(1)
    
    def convert_units(self):
        try:
            value = float(self.unit_value.get())
            from_u = self.from_unit.get()
            to_u = self.to_unit.get()
            conv_type = self.conversion_type.get()
            
            if conv_type == 'Temperature':
                result = self.convert_temperature(value, from_u, to_u)
            elif conv_type == 'Weight':
                result = self.convert_weight(value, from_u, to_u)
            else:
                result = self.convert_length(value, from_u, to_u)
            
            self.unit_result.config(
                text=f'✓  {value} {from_u} = {result:.4f} {to_u}',
                bg='#e8f5e9',
                fg='#2e7d32'
            )
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid number!')
    
    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == 'Fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'Kelvin':
            celsius = value - 273.15
        else:
            celsius = value
        
        if to_unit == 'Fahrenheit':
            return celsius * 9/5 + 32
        elif to_unit == 'Kelvin':
            return celsius + 273.15
        return celsius
    
    def convert_weight(self, value, from_unit, to_unit):
        to_kg = {'Kilograms': 1, 'Pounds': 0.453592, 'Grams': 0.001, 'Ounces': 0.0283495}
        kg_value = value * to_kg[from_unit]
        return kg_value / to_kg[to_unit]
    
    def convert_length(self, value, from_unit, to_unit):
        to_meters = {'Meters': 1, 'Feet': 0.3048, 'Kilometers': 1000, 
                     'Miles': 1609.34, 'Centimeters': 0.01, 'Inches': 0.0254}
        meter_value = value * to_meters[from_unit]
        return meter_value / to_meters[to_unit]
    
    # ============================================
    # TAB 3: AGE CALCULATOR
    # ============================================
    def create_age_calculator_tab(self):
        age_frame = tk.Frame(self.notebook, bg='#f5f5f5')
        self.notebook.add(age_frame, text='📅  Age Calculator')
        
        container = tk.Frame(age_frame, bg='#ffffff')
        container.place(relx=0.5, rely=0.5, anchor='center', width=550, height=500)
        
        tk.Label(
            container,
            text='🎂 Age Calculator',
            font=('Arial', 22, 'bold'),
            bg='#ffffff',
            fg='#16213e'
        ).pack(pady=(30, 30))
        
        # Date inputs
        input_frame = tk.Frame(container, bg='#f8f9fa')
        input_frame.pack(pady=20, padx=40, fill='x')
        
        tk.Label(input_frame, text='Enter Your Birth Date', font=('Arial', 13, 'bold'),
                bg='#f8f9fa', fg='#16213e').pack(pady=(20, 15))
        
        dob_frame = tk.Frame(input_frame, bg='#f8f9fa')
        dob_frame.pack(pady=15)
        
        # Day
        tk.Label(dob_frame, text='Day', font=('Arial', 10), bg='#f8f9fa').grid(row=0, column=0, padx=10)
        self.birth_day = tk.Spinbox(dob_frame, from_=1, to=31, width=8, font=('Arial', 12),
                                    relief=tk.FLAT, bd=2, highlightthickness=1)
        self.birth_day.grid(row=1, column=0, padx=10, pady=5)
        
        # Month
        tk.Label(dob_frame, text='Month', font=('Arial', 10), bg='#f8f9fa').grid(row=0, column=1, padx=10)
        self.birth_month = tk.Spinbox(dob_frame, from_=1, to=12, width=8, font=('Arial', 12),
                                      relief=tk.FLAT, bd=2, highlightthickness=1)
        self.birth_month.grid(row=1, column=1, padx=10, pady=5)
        
        # Year
        tk.Label(dob_frame, text='Year', font=('Arial', 10), bg='#f8f9fa').grid(row=0, column=2, padx=10)
        self.birth_year = tk.Spinbox(dob_frame, from_=1900, to=2025, width=10, font=('Arial', 12),
                                     relief=tk.FLAT, bd=2, highlightthickness=1)
        self.birth_year.delete(0, tk.END)
        self.birth_year.insert(0, '2000')
        self.birth_year.grid(row=1, column=2, padx=10, pady=5)
        
        input_frame.pack_configure(pady=(20, 10))
        
        self.create_modern_button(container, '📊 Calculate Age', self.calculate_age, '#9c27b0', 18).pack(pady=25)
        
        # Result
        self.age_result = tk.Label(
            container,
            text='Your age will be displayed here',
            font=('Arial', 12),
            bg='#f3e5f5',
            fg='#6a1b9a',
            justify=tk.LEFT,
            relief=tk.FLAT,
            pady=20
        )
        self.age_result.pack(fill='x', padx=40, pady=(10, 30))
    
    def calculate_age(self):
        try:
            day = int(self.birth_day.get())
            month = int(self.birth_month.get())
            year = int(self.birth_year.get())
            
            birth_date = datetime(year, month, day)
            today = datetime.now()
            
            years = today.year - birth_date.year
            months = today.month - birth_date.month
            days = today.day - birth_date.day
            
            if days < 0:
                months -= 1
                prev_month = today.month - 1 if today.month > 1 else 12
                days_in_prev = [31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][prev_month - 1]
                days += days_in_prev
            
            if months < 0:
                years -= 1
                months += 12
            
            total_days = (today - birth_date).days
            
            result_text = f'''
✓ Years: {years}  |  Months: {months}  |  Days: {days}

📊 Total Days Lived: {total_days:,}
📅 Total Months: {years * 12 + months}
            '''
            
            self.age_result.config(text=result_text, bg='#e8f5e9', fg='#2e7d32')
            
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid date!')
    
    # ============================================
    # TAB 4: BMI CALCULATOR
    # ============================================
    def create_bmi_calculator_tab(self):
        bmi_frame = tk.Frame(self.notebook, bg='#f5f5f5')
        self.notebook.add(bmi_frame, text='⚖️  BMI Calculator')
        
        container = tk.Frame(bmi_frame, bg='#ffffff')
        container.place(relx=0.5, rely=0.5, anchor='center', width=550, height=500)
        
        tk.Label(
            container,
            text='💪 BMI Calculator',
            font=('Arial', 22, 'bold'),
            bg='#ffffff',
            fg='#16213e'
        ).pack(pady=(30, 25))
        
        # Input frame
        input_frame = tk.Frame(container, bg='#f8f9fa')
        input_frame.pack(pady=20, padx=40, fill='x')
        
        tk.Label(input_frame, text='Enter Your Details', font=('Arial', 13, 'bold'),
                bg='#f8f9fa', fg='#16213e').pack(pady=(20, 20))
        
        # Weight
        weight_frame = tk.Frame(input_frame, bg='#f8f9fa')
        weight_frame.pack(pady=10)
        
        tk.Label(weight_frame, text='Weight:', font=('Arial', 11, 'bold'),
                bg='#f8f9fa', fg='#16213e', width=10, anchor='w').pack(side=tk.LEFT, padx=5)
        
        self.weight_entry = self.create_modern_entry(weight_frame, 15)
        self.weight_entry.pack(side=tk.LEFT, padx=5, ipady=5)
        
        self.weight_unit = ttk.Combobox(weight_frame, values=['kg', 'lbs'],
                                       font=('Arial', 10), state='readonly', width=8)
        self.weight_unit.pack(side=tk.LEFT, padx=5)
        self.weight_unit.current(0)
        
        # Height
        height_frame = tk.Frame(input_frame, bg='#f8f9fa')
        height_frame.pack(pady=10)
        
        tk.Label(height_frame, text='Height:', font=('Arial', 11, 'bold'),
                bg='#f8f9fa', fg='#16213e', width=10, anchor='w').pack(side=tk.LEFT, padx=5)
        
        self.height_entry = self.create_modern_entry(height_frame, 15)
        self.height_entry.pack(side=tk.LEFT, padx=5, ipady=5)
        
        self.height_unit = ttk.Combobox(height_frame, values=['cm', 'meters', 'feet'],
                                       font=('Arial', 10), state='readonly', width=8)
        self.height_unit.pack(side=tk.LEFT, padx=5)
        self.height_unit.current(0)
        
        input_frame.pack_configure(pady=(20, 5))
        
        self.create_modern_button(container, '⚡ Calculate BMI', self.calculate_bmi, '#ff5722', 18).pack(pady=25)
        
        # Result
        self.bmi_result = tk.Label(
            container,
            text='Your BMI will be displayed here',
            font=('Arial', 12),
            bg='#fff3e0',
            fg='#e65100',
            justify=tk.LEFT,
            relief=tk.FLAT,
            pady=20
        )
        self.bmi_result.pack(fill='x', padx=40, pady=(10, 30))
    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            if self.weight_unit.get() == 'lbs':
                weight *= 0.453592
            
            height = float(self.height_entry.get())
            if self.height_unit.get() == 'cm':
                height /= 100
            elif self.height_unit.get() == 'feet':
                height *= 0.3048
            
            bmi = weight / (height ** 2)
            
            if bmi < 18.5:
                category, color, bg = 'Underweight', '#ff9800', '#fff3e0'
            elif bmi < 25:
                category, color, bg = 'Normal (Healthy)', '#4caf50', '#e8f5e9'
            elif bmi < 30:
                category, color, bg = 'Overweight', '#ff9800', '#fff3e0'
            else:
                category, color, bg = 'Obese', '#f44336', '#ffebee'
            
            result_text = f'''
✓ Your BMI: {bmi:.2f}

📊 Category: {category}

Weight: {weight:.1f} kg  |  Height: {height:.2f} m
            '''
            
            self.bmi_result.config(text=result_text, bg=bg, fg=color)
            
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numbers!')


# Run the application
if __name__ == '__main__':
    root = tk.Tk()
    app = ModernMultiApp(root)
    root.mainloop()


# Leave Management
  

This module is will be used in Technical testing only and not allowed for public use

  

## Prerequisites

    

  

-  **Odoo 18.0** installed and running on your system.

- Basic knowledge of Odoo and its folder structure.

- Python 3.7+ (check Odoo 18 requirements for exact version support).

- Required Python dependencies installed.

  

## Installation Guide

  

### 1. Clone the Module Repository

  

If you have the module stored in a Git repository, clone it to your local Odoo add-ons directory.

  

```bash
cd  /path/to/your/odoo/custom_addons
git  clone  https://github.com/yourusername/leave_management.git
```
### 2. Install Required Python Libraries

If your module requires additional Python libraries, install them via `pip`.

If your OS is debian it is recommended to install dependencies by setup/debinstall.sh by running
```bash
cd /path/to/your/odoo
bash ./setup/debinstall.sh
```
Otherwise you can install dependencies by
```bash
pip install -r requirements.txt` 
```

### 3. Configure the Module in Odoo

1.  Open the Odoo configuration file (`odoo.conf` or similar).
    
2.  Add the module directory to the `addons_path`:
    
    `addons_path = addons,custom_addons` 
    

### 4. Update App List and Install Module

1.  Restart the Odoo service to recognize the new module.
    
2.  Log in to the Odoo web interface.
    
3.  Go to **Apps** and click **Update Apps List**.
    
4.  Search for **Leave Management** and click **Install**.
    

## Usage

Once installed, navigate to the **Leave Management** menu in the Odoo dashboard to:

-   Apply for leave
-   Approve or reject leave requests
-   View leave history
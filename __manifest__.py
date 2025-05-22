# __manifest__.py
{
    "name": "Employee Self Service Portal",
    "version": "1.0",
    "depends": ["portal", "hr", "hr_attendance", "om_hr_payroll", "hr_holidays"],
    "category": "Human Resources",
    "summary": "Allow employees to access and manage their information via portal access.",
    "data": [
        "security/ir.model.access.csv",
        "security/portal_employee_security.xml",
        "views/menu.xml",
        "views/portal_layout.xml",
        "views/portal_employee_templates.xml",
        "views/portal_attendance_templates.xml",
        "data/portal_data.xml"
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
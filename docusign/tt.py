import frappe

def show_hello_message(doc, method):
    # Show a message when a Sales Invoice is submitted
    frappe.msgprint("Hello")
    
from frappe.desk.form.utils import get_pdf_link
from frappe.utils import get_link_to_form
from frappe import _


def on_submit(self,method):
    documents = get_digital_signature_documents(self.doctype)
    if documents:
        for print_format,workflow in documents.items():
            doc = frappe.new_doc(f"DSC {self.doctype}")
            # doc = frappe.new_doc("Digital Signature")
            doc.document_type = self.doctype
            doc.document = self.name
            doc.print_format = print_format
            doc.workflow = workflow
            doc.pdf_document = get_pdf_link(self.doctype, self.name, print_format)
            doc.save()
            doc.submit() 
            frappe.msgprint(_("Created a new digital signature document {0}").format(get_link_to_form(f"DSC {self.doctype}", doc.name)))
            
def get_digital_signature_documents(doctype):
    documents = frappe.db.sql(f"select print_format,workflow from `tabDigital Signature Document` where document_type = '{doctype}'",as_dict=True)
    #document_list =  [d for document in documents for d in document]
    document_dict = {document.print_format:document.workflow for document in documents}
    return document_dict
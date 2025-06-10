from proxy import DocumentProxy


admin_doc = DocumentProxy("classified.txt", user="admin")
guest_doc = DocumentProxy("classified.txt", user="guest")

print("Admin trying to view document:")
admin_doc.display()
admin_doc.display()
admin_doc.display()

print("\nGuest trying to view document:")
guest_doc.display()
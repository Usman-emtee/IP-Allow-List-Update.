import os

def update_allow_list(import_file, remove_list):
    """Update allow_list.txt by removing IPs in remove_list."""
    # Open and read the allow list file
    with open(import_file, "r") as file:
        ip_addresses = file.read()
    
    # Convert string to list
    ip_addresses = ip_addresses.split()
    
    # Remove IPs from remove_list
    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)
    
    # Convert list back to string
    ip_addresses = "\n".join(ip_addresses)
    
    # Write updated list back to file
    with open(import_file, "w") as file:
        file.write(ip_addresses)
    
    return ip_addresses

def main():
    # Sample remove list
    remove_list = ["192.168.1.100", "10.0.0.50"]
    import_file = "data/allow_list.txt"
    
    # Create sample allow_list.txt if it doesn't exist
    if not os.path.exists(import_file):
        with open(import_file, "w") as file:
            file.write("192.168.1.1\n192.168.1.100\n10.0.0.50\n172.16.0.10")
    
    # Update allow list
    updated_ips = update_allow_list(import_file, remove_list)
    print("Updated Allow List:")
    print(updated_ips)
    
    # Save updated list for evidence
    with open("data/updated_allow_list.txt", "w") as file:
        file.write(updated_ips)

if __name__ == "__main__":
    main()
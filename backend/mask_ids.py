import re

def mask_unique_id(text):
    # Define patterns to match various formats of unique IDs
    id_patterns = [
        r'\b\d{4}-\d{4}-\d{4}-\d{4}\b',    # Example for IDs like 1234-5678-9012-3456
        r'\b\d{16}\b',                      # Example for 16-digit IDs
        r'\b\d{6}-\d{5}\b'                  # Example for IDs like 123456-12345
    ]
    
    masked_text = text
    
    for pattern in id_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            # Mask all but the last 4 digits
            masked_id = '*' * (len(match) - 4) + match[-4:]
            masked_text = masked_text.replace(match, masked_id)
    
    # Replace any other sensitive information with asterisks
    # This could be expanded based on the specific formats of sensitive data
    sensitive_patterns = [
        r'\b\d{3}-\d{2}-\d{4}\b',           # Example for social security numbers (SSNs) like 123-45-6789
        r'\b\d{4} \d{4} \d{4} \d{4}\b',      # Example for credit card numbers
        # Add more patterns as needed
    ]
    
    for pattern in sensitive_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            masked_sensitive = '*' * len(match)
            masked_text = masked_text.replace(match, masked_sensitive)
    
    return masked_text

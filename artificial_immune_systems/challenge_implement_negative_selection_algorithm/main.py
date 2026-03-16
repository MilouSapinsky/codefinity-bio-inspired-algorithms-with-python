import random

# --- Defining Helper Function ---
def generate_random_pattern(length):
    """Generates a random binary string of a given length."""
    return ''.join(random.choice(['0', '1']) for _ in range(length))

# --- Defining the Core NSA Functions ---
def generate_detectors(self_patterns, num_detectors):
    """Generates a set of detectors that are not in the self_patterns set."""
    length = len(self_patterns[0])
    detectors = set()
    self_set = set(self_patterns)
    attempts = 0
    # Limiting attempts to avoid an infinite loop if num_detectors is too large
    while len(detectors) < num_detectors and attempts < num_detectors * 100:
        candidate = generate_random_pattern(length)
        
        # 1. Checking if the candidate is "non-self"
        if candidate not in self_set:
            detectors.add(candidate)
        attempts += 1
    return list(detectors)

def classify_patterns(self_patterns, detectors, test_patterns):
    """Classifies test patterns as 'self' or 'non-self'."""
    self_set = set(self_patterns)
    detector_set = set(detectors)
    results = {}
    
    for pattern in test_patterns:
        # 2. Implementing the classification logic
        if pattern in self_set:
            results[pattern] = 'self'
        elif pattern in detector_set:
            results[pattern] = 'non-self'
        else:
            results[pattern] = 'non-self'
            
    return results

# --- Running the Algorithm ---

# Setting a seed for reproducible results
random.seed(42)

self_patterns = ["0101", "1100", "1001"]
test_patterns = ["0000", "0101", "1111", "1001", "1010"]
num_detectors = 6 # We'll generate 6 detectors

# Generating detectors
detectors = generate_detectors(self_patterns, num_detectors)

# Classifying the test patterns
results = classify_patterns(self_patterns, detectors, test_patterns)

# --- Displaying the Results ---
print(f"Self Patterns: {self_patterns}")
print(f"Generated Detectors: {detectors}")
print("\n--- Classification Results ---")
for pattern in test_patterns:
    print(f"{pattern}: {results.get(pattern)}")
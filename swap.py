def swap(v1, v2):
    temp = v1
    v1 = v2
    v2 = temp
    return v1, v2

# Example usage:
v1 = 'a'
v2 = 1
v1, v2 = swap(v1, v2)

print(f"v1 = {v1}, v2 = {v2}")

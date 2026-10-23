def replace_value(values, index, new_value):
    values[index] = new_value
    return None

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return 1
    return -1

def summarize(values):
    stats_record = (min(values), max(values), sum(values))
    return stats_record


days = int(input("Enter the number of days: "))

original = []

for _ in range(days):
    emails = int(input("Enter the number of emails received: "))
    original.append(emails)


updated = original[:]

correct_index = int(input("Enter the index to correct: "))
new_emails = int(input("Enter the new number of emails: "))
replace_value(updated, correct_index, new_emails )

target = int(input("Enter the number of emails to search for: "))

first_index = find_first(updated, target)
matching_count = updated.count(target)

minimum, maximum, total = summarize(updated)

sorted_list = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum number of emails: {minimum}")
print(f"Maximum number of emails: {maximum}")
print(f"Total number of emails: {total}")

if first_index != -1:
    print(f"First matching index: {first_index}")

else:
    print(f"Target not found")

print(f"Matching values: {matching_count}")
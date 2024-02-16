from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv


# Task 1:
def union(text):
  for i in range(1, len(text)):
    new_list = text[i][:3]
    new_list = " ".join(new_list).strip().split()
    for j in range(0, len(new_list)):
      text[i][j] = new_list[j]
  return text


# Task 2:
def normalization_number(phone):
  pattern = r"(\+7|8)?\s*\(?(\d{2,3})\)?\s*(\d{2,3})*[-\s]*(\d{2,3})[-\s]*(\d{2,3})\s*\(*(доб\.)*\s*(\d+)*\)*"
  substitute = r"+7(\2)\3-\4-\5 \6\7"
  for i in range(1, len(phone)):
    resul = re.sub(pattern, substitute, phone[i][5])
    phone[i][5] = resul.strip()
  return phone

# Task 3:
def dublicates(data):
  my_dict = {}
  for row in contact_list:
    key = row[0] + " " + row[1]
    if key not in my_dict:
      my_dict[key] = row[2:]
    else:
      for i in range(5):
        if not my_dict[key][i]:
          my_dict[key][i] += row[i+2]

  resul = []
  for key, value in my_dict.items():
    key = key.split()
    key.extend(value)
    resul.append(key)
  return resul






if __name__ == '__main__':
    with open('phonebook_raw.csv', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        contact_list = list(rows)

    new_file = union(contact_list)
    new_file = normalization_number(new_file)
    new_file = dublicates(new_file)

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        data_writer = csv.writer(f, delimiter=',', lineterminator="\r")
        data_writer.writerows(new_file)
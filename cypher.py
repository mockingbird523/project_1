alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(original_text, shift_amount,shift_direction):
   final_text = ""
   if shift_direction =="decode":
      shift_amount*=-1
   for letter in original_text:
      if letter in alphabet:
         position = alphabet.index(letter)
         new_position = (position + shift_amount) % len(alphabet)
         final_text += alphabet[new_position]
      else:
         final_text += letter
   print(f"The {shift_direction}d text is: {final_text}")
      
caesar(original_text=text,shift_amount=shift, shift_direction=direction)






















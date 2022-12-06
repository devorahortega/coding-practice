# Write a function that returns the reverse of a given string.

# Input = ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]

def reverse(array)
    index = array.length - 1
    result = []

    while index >= 0
        result.push(array[index])
        index -= 1
    end

    return result
end 

p reverse(["h", "e", "l", "l", "o"])

# Define the string 
# create a loop .each do
# shift first to last until string is done


# Input: "hello" 
# Output: "olleh"
file_name = "/sampletext.txt"

# Reads in a file
def read_file(file_name):

    with open(file_name) as f:
        contents = f.read()
        print(contents)
        
        return contents
        raise NotImplementedError()


# Reads in a file and stores each line as an element in a list
def read_file_into_list(file_name):
    with open (file_name) as f:

        return f.readlines()
        raise NotImplementedError()


# Writes the first line of a string to a file.
def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split("\n")[0]

    with open(output_filename, 'w') as f:
        f.write(first_line)
        
        return
        raise NotImplementedError()


# Reads in the even numbered lines of a file
def read_even_numbered_lines(file_name):
    with open (file_name) as f:
        lines = f.readlines()
        
        return [line for idx, line in enumerate(lines) if (idx + 1) % 2 == 0]
        raise NotImplementedError()


# Reads a file and returns a list of the lines in reverse order
def read_file_in_reverse(file_name):
    with open(file_name) as f:
        
        return f.readlines()[::-1]
        raise NotImplementedError()


# test implementation
def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
import sys
import os
import io

DEBUG = False

def fileopen(input_file):
    encodings = ["utf-32", "utf-16", "utf-8", "cp1252", "gb2312", "gbk", "big5"]
    tmp = ''
    for enc in encodings:
        try:
            with io.open(input_file, mode="r", encoding=enc) as fd:
                tmp = fd.read()
                break
        except:
            if DEBUG:
                print(enc + ' failed')
            continue
    return [tmp, enc]

def styleCopy(input_filepath, output_filepath):
    if '.ass' not in input_filepath or '.ass' not in output_filepath:
        print("One of those files is not an ass file")
        return input_filepath

    if not os.path.isfile(input_filepath) or not os.path.isfile(output_filepath):
        print("One of those files does not exist")
        return

    src = fileopen(input_filepath)
    content_input = src[0]
    content_input = content_input.split('\n')
    encoding_input = src[1]
    
    src = fileopen(output_filepath)
    content_ouput = src[0]
    content_ouput = content_ouput.split('\n')
    encoding_output = src[1]

    for line_count in range(len(content_input)):
        line_input = content_input[line_count]
        if (line_input.startswith("Dialogue")):
            line_ouput = content_ouput[line_count]
            splitted_line_input = line_input.split(',')
            splitted_line_output = line_ouput.split(',')
            splitted_line_output[3] = splitted_line_input[3]
            content_ouput[line_count] = ",".join(splitted_line_output)

    content_ouput = '\n'.join(content_ouput)
    with io.open(output_filepath, 'w') as output:
        output.write(content_ouput)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        styleCopy(sys.argv[1], sys.argv[2])
    else:
        print("Usage: " + sys.argv[0] + " input_filepath output_filepath")

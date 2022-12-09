file_test = open("2022/data/2022-7-test.txt")
lines_test=file_test.readlines()
file = open("2022/data/2022-7.txt")
lines = file.readlines()
import json
line_n=0
size=0
def sum_folderfs(lines):
    folders={'/':[]}
    index=[]
    size=0
    for line in lines:
        line_v=line.strip("\n")
        if line_v[0]=='$':
            command=line_v.split(" ")
            #print(command)
            if command[1] == 'cd':
                if command[2]=='/':
                    index=[]
                elif command[2] == "..":
                    index.pop()
                    #print("{} going into {}".format(line_v, index))

                else:
                    index.append(command[2])
                    folders["/"+"/".join(index)] = []
                    #print("{} going into {}".format(line_v, command[2]))

        if line_v[0] == 'dir':
            pass
        if line_v[0] in '1234567890':
            sizeandfilename=line_v.split(" ")
            folders["/"+"/".join(index)].append({sizeandfilename[1] :int(sizeandfilename[0])})
    #print(str(json.dumps(folders,indent=4)))

    folders_size={}
    for folder in folders:
        sum_f=0

        for file in folders[folder]:
            sum_fi = 0
            for _,size_f in file.items():
                sum_fi += size_f
            sum_f+=sum_fi
        #print("Folder {} : {}".format(folder,sum_f))
        folders_size[folder]=sum_f

    folder_size_total={}
    for folder in folders_size:
        folder_size_total[folder]=folders_size[folder]
        for folder_2 in folders_size:
            #print("{} and {}".format(folder,folder_2 ))
            if folder_2.startswith(folder) and folder_2 != folder:
                #print("{} in {}".format(folder_2,folder ))
                if folder in folder_size_total:
                    folder_size_total[folder]=folder_size_total[folder]+folders_size[folder_2]
                else:
                    folder_size_total[folder]=folders_size[folder_2]
    #print(str(json.dumps(folder_size_total,indent=4)))
    smallest_size=70000000
    size_avail=70000000-42558312
    size_to_find=30000000-size_avail
    print("Finding ... "+str(size_to_find))
    for foldern,size_f in folder_size_total.items():
        if size_f <= 100000:
            size+=size_f
        if size_to_find < size_f and size_f < smallest_size:
            smallest_size = size_f

    print("smallest : {} (wrong : 36092)".format(smallest_size)       )
    return size

print("PART 2 EXAMPLE : {} == 95437".format(sum_folderfs(lines_test)))
print("PART 2 PUZZLE  : {}  ".format(sum_folderfs(lines)))

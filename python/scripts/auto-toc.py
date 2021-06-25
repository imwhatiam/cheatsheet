import os
import copy

out_put = []
md_str = '* [%s](%s)'
blank_prefix = '  '


def is_md_file(filename):
    return filename.endswith('.md') or filename.endswith('.markdown')


for root, dirs, files in os.walk("."):
    out_put_copy = copy.deepcopy(out_put)
    md_files = [filename for filename in files if is_md_file(filename)]
    for name in dirs + md_files:
        if name.startswith('.') or \
                name in ['seacloud.cc', 'AWS', 'seafile']:
            continue

        path = os.path.join(root, name)

        if not out_put_copy:
            out_put.append(path)
        else:
            compared_indexs = -1
            for idx, val in enumerate(out_put_copy):
                if path.startswith(val):
                    compared_indexs = idx

            if compared_indexs >= 0:
                out_put.insert(compared_indexs + 1, path)

with open('SUMMARY.md', 'w') as f:
    for path in out_put:
        if path.endswith('SUMMARY.md'):
            continue

        path = path.replace(' ', '&#32;')
        name = os.path.basename(path)
        level = len(path.split('/')) - 2
        if level == 0:
            line = md_str % (name, path)
        else:
            line = level * blank_prefix + md_str % (name, path)
        f.write(line + '\n')

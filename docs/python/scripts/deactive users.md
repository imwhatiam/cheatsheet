要在 shell 脚本中对每个 email 发送一个 HTTP PUT 请求，你可以将 `curl` 命令嵌入到 `for` 循环中。以下是一个示例脚本，展示了如何对每个 email 地址执行 `curl` 请求。

### 脚本示例

```bash
#!/bin/bash

# 指定文件名
file="emails.txt"

# API 请求的基础 URL 和 Token
base_url="https://cloud.seafile.com/api/v2.1/admin/users"
token="f2d84d433a7d6a255e27f325c1050df48e8c26ac"

# 使用 while 循环逐行读取文件
while IFS= read -r email
do
  # 构造 curl 命令
  curl -X PUT \
    -d "is_active=false" \
    -H "Authorization: Token $token" \
    -H "Accept: application/json; charset=utf-8; indent=4" \
    "$base_url/$email/"
  
  # 可选：在每次请求后添加一个输出，便于跟踪处理进度
  echo "Processed email: $email"
done < "$file"
```

### 脚本说明

1. **变量声明**:
   - `file="emails.txt"`: 指定包含 email 地址的文件名。
   - `base_url`: API 的基础 URL。
   - `token`: 用于授权的 API Token。

2. **读取文件**:
   - `while IFS= read -r email`: 使用 `while` 循环逐行读取文件中的 email 地址。

3. **发送 `curl` 请求**:
   - `curl -X PUT`：使用 `curl` 命令发送 HTTP PUT 请求。
   - `-d "is_active=false"`：设置请求体数据，这里将 `is_active` 字段设置为 `false`。
   - `-H "Authorization: Token $token"`：添加请求头，用于认证。
   - `-H "Accept: application/json; charset=utf-8; indent=4"`：设置请求头，指定接受的响应类型为 JSON。
   - `"$base_url/$email/"`: 构造请求的完整 URL，包含 email 地址。

4. **处理输出**:
   - `echo "Processed email: $email"`：可选，用于输出每次处理的 email，便于跟踪脚本的执行过程。

### 运行脚本

1. **创建文件**: 创建一个包含 email 地址的文件，例如 `emails.txt`，每行一个 email。

   ```
   email1@example.com
   email2@example.com
   email3@example.com
   ```

2. **保存脚本**: 将上述脚本保存到一个文件中，比如 `process_emails.sh`。

3. **给予执行权限**: 使脚本可执行。

   ```bash
   chmod +x process_emails.sh
   ```

4. **运行脚本**:

   ```bash
   ./process_emails.sh
   ```

确保你在实际使用脚本之前，已经检查了所有的请求参数和 API URL 的正确性，以避免意外的更改或错误。
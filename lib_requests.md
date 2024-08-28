### Web开发与网络编程

#### HTTP请求与响应

##### requests库的基本使用

在Python的Web开发与网络编程中，处理HTTP请求与响应是核心技能之一。`requests`库是Python中一个强大且易用的HTTP库，广泛应用于发送HTTP请求和处理响应。以下是对`requests`库基本使用的展开介绍：

1. **安装requests库**：
   使用`pip`安装`requests`库：
   ```bash
   pip install requests
   ```

2. **发送HTTP请求**：
   `requests`库支持多种HTTP方法，如`GET`、`POST`、`PUT`、`DELETE`等。发送HTTP请求的基本格式如下：
   ```python
   import requests

   response = requests.get('https://example.com')
   ```
   上述代码发送了一个`GET`请求到指定的URL，并将服务器返回的响应存储在`response`对象中。

3. **处理响应**：
   `requests`库返回的响应对象包含多个属性和方法，用于访问服务器返回的数据。例如：
   ```python
   # 获取响应状态码
   status_code = response.status_code
   print(f"Status Code: {status_code}")

   # 获取响应内容
   content = response.text
   print(f"Response Content: {content}")

   # 获取响应的JSON格式数据（如果存在）
   json_data = response.json()  # 如果响应内容是JSON格式
   print(f"JSON Data: {json_data}")
   ```
   - `status_code`：获取HTTP响应的状态码，如`200`表示请求成功。
   - `text`：获取响应内容，通常是HTML或JSON等格式的字符串。
   - `json()`：直接将响应内容解析为JSON对象（前提是响应内容为JSON格式）。

4. **发送带参数的请求**：
   可以通过`params`参数向`GET`请求添加查询参数：
   ```python
   payload = {'key1': 'value1', 'key2': 'value2'}
   response = requests.get('https://example.com', params=payload)
   print(response.url)  # 打印请求的完整URL
   ```
   这种方式会将查询参数自动添加到URL的末尾。

5. **发送POST请求**：
   使用`POST`方法可以将数据发送到服务器。例如：
   ```python
   data = {'key1': 'value1', 'key2': 'value2'}
   response = requests.post('https://example.com', data=data)
   print(response.text)
   ```
   `POST`请求通常用于提交表单数据或上传文件。

6. **处理请求异常**：
   `requests`库提供了异常处理机制来应对网络请求中的错误：
   ```python
   try:
       response = requests.get('https://example.com', timeout=5)
       response.raise_for_status()  # 检查是否有HTTP错误
   except requests.exceptions.HTTPError as err:
       print(f"HTTP error occurred: {err}")
   except requests.exceptions.ConnectionError as err:
       print(f"Error connecting: {err}")
   except requests.exceptions.Timeout as err:
       print(f"Timeout error: {err}")
   except requests.exceptions.RequestException as err:
       print(f"An error occurred: {err}")
   ```
   - `timeout`参数设置请求的超时时间。
   - `raise_for_status()`方法用于检查响应的状态码是否引发异常。

通过对`requests`库的基本使用掌握，你可以轻松地在Python中处理各种HTTP请求与响应，适用于Web开发与网络编程的各种场景。

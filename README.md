# SUSTech_Class_Schedule_to_ics_Conventor

用于将南方科技大学tis系统上的课程表转换为ics格式。

Intent to convert the timetable on the SUSTech tis system to ics format.

## 如何运行

### 获取课程表json

登陆tis系统（[https://tis.sustech.edu.cn/](https://tis.sustech.edu.cn/)）后，进入选课页面，打开开发者工具（`F12`）的“Network”标签页，点击“查看课表”，观察下方窗口中出现的`queryXskbcxList`项目，将该请求另存为json文件并重命名为`data.json`。

以下是使用curl将其存储为json的一个例子。

```bash
curl 'https://tis.sustech.edu.cn/Xskbcx/queryXskbcxList' \
  -H 'authority: tis.sustech.edu.cn' \
  -H 'accept: */*' \
  -H 'dnt: 1' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'rolecode: 01' \
  -H 'origin: https://tis.sustech.edu.cn' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://tis.sustech.edu.cn/Xsxk/query/1' \
  -H 'cookie: Secure; route=xxx; JSESSIONID=xxx; Secure' \
  --data-raw 'bs=2&xn=2020-2021&xq=2' \
  --compressed > data.json
```

### 修改周历

根据该学期校历，修改`2020-2021-2.csv`。

### 运行

```bash
conda env create -f environment.yml
python3 main.py
```

将会输出名为`schedule.ics`的日历文件。

将课程表添加至电子设备的流程请参考此链接：[https://sustech.online/service/blackboard/retrive-ics-url/](https://sustech.online/service/blackboard/retrive-ics-url/)


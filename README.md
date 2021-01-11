## 绩效管理系统-后端
一个基于Flask+vue-element-admin前后端分离的绩效管理系统  
[![](https://img.shields.io/badge/license-MIT-green)](https://github.com/run-nerver/performance-management-frontend/blob/main/LICENSE)
[![](https://img.shields.io/badge/flask-1.1.2-brightgreen)](https://github.com/pallets/flask)
[![](https://img.shields.io/badge/vue-2.6.10-brightgreen.svg?style=flat-square)](https://github.com/vuejs/vue)
[![](https://img.shields.io/badge/vue--element--admin-4.3.1-brightgreen)](https://panjiachen.github.io/vue-element-admin-site/zh/) 

## 说明
此为后端代码，对应前端代码请移步[绩效管理系统-前端](https://github.com/run-nerver/performance-management-frontend)


## 使用方法
### 本地测试
#### 后端
1、修改my_jixiao_backend/app/config/settings.py中SQLALCHEMY_DATABASE_URI为自己数据库地址 

2、数据库中运行jixiao_zhanshi.sql文件，添加测试数据 

3、
```
cd performance-management-backend
pip install -r requirements.txt
flask run -p 7000
``` 

#### 前端([源码](https://github.com/run-nerver/performance-management-frontend))
```
cd performance-management-frontend
npm i
npm run dev
```  
确保数据库数据正确加载后，使用账号登陆
```
账号：10000
密码：123456
``` 

### Docker
#### 后端
1、修改performance-management-backend/app/config/settings.py中SQLALCHEMY_DATABASE_URI为自己数据库地址 

2、数据库中运行jixiao_zhanshi.sql文件，添加测试数据 

3、
```dockerfile
cd performance-management-backend
docker image build -t performance-management-backend:1 .
docker run -it -d -p 7000:7000 performance-management-backend:1
``` 
#### 前端([源码](https://github.com/run-nerver/performance-management-frontend))
```dockerfile
cd performance-management-frontend
npm i 
npm run build:prod
docker image build -t performance-management-frontend:1 .
docker run -it id 7001:80 performance-management-frontend:1
```
确保数据库数据正确加载后，浏览器访问http://127.0.0.1:7001，使用账号登陆
```
账号：10000
密码：123456
```  
## 部分截图
![](http://pic.tongxunkeji.cn/%E9%A6%96%E9%A1%B5.png)  

![](http://pic.tongxunkeji.cn/%E6%95%99%E5%AD%A6%E5%B7%A5%E4%BD%9C%E9%87%8F.png)  

![](http://pic.tongxunkeji.cn/%E6%95%99%E5%B8%88%E6%80%BB%E8%A1%A8.png)  

![](http://pic.tongxunkeji.cn/%E5%8F%82%E6%95%B0%E8%AE%BE%E7%BD%AE.png)  

![](http://pic.tongxunkeji.cn/%E7%A7%91%E7%A0%94%E5%B7%A5%E4%BD%9C%E9%87%8F.png)  

## 其他说明
绩效分配规则对应每个使用部门的规则都不一样，此开源系统仅供参考，适合相关人员进行二次开发。不适用于所有业务逻辑。  

## License
[MIT](https://opensource.org/licenses/MIT)

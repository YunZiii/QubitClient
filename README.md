# QubitClient

#### 介绍
**qubit-client**
QubitClient 是用于使用Qubit服务的示例。

#### 使用说明
1.拷贝config.py.example文件为config.py，并修改配置参数。
```
cp config.py.example config.py
```
2.运行
```Python
python client_demo.py
```

#### 请求输入

```python
response = client.request(file_list=dict_list)
```
dict_list格式为：
```json
[
    {
        "bias":np.ndarray shape(A),
        "frequency":np.ndarray shape(B),
        "iq_avg":np.ndarray shape(B,A),
    },
    ...
]
```


#### 返回值
返回请求为response
```python
res = response.json()
```
res格式为：
```json
{
    "state":'success',
    "result":result
}
```
其中result格式：
```json
[
    {
        "params_list":List[List[float]],//每条线段的多项式参数列表
        "linepoints_list":List[List[[row_index,col_index]]],//每条线段的点坐标列表
        "confidence_list":List[float],//每条线段的置信度
    },//每一个npz文件的结果
    {
        ...
    },
    ...
]
```

### 坐标映射
```python
points = result[0]["linepoints_list"][0]
reflection_points = client.convert_axis(points, bias,frequency)
```
`points`格式:`List[[row_index,col_index],...]`,表示单条线段的点坐标.<br>
`bias`格式:`np.ndarray shape(A)`，与上述bias相同.<br>
`frequency`格式:`np.ndarray shape(B)`，与上述frequency相同.<br>


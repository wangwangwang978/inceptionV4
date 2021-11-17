# 基于MindSpore AI框架实现零售商品识别

# 第一步 导入代码和测试集（如下为文件结构）
![image](https://user-images.githubusercontent.com/67614464/142162066-251dced8-4b1c-44e2-bdd7-c1c9572b04e5.png)

# 第二步
## 进入工作目录
cd inceptionv4
## 数据增广，裁剪，旋转等
python preprocess.py
## 安装第三方库
pip install -r requirements.txt
## 开始训练
python train.py --config_path="default_config.yaml" --device_id 0  --dataset_path=data
## 测试最高迭代次数的训练文件（这里为50次，可在ckpts_rank_0文件夹看到）
python eval.py --config_path="default_config.yaml" --platform=Ascend --dataset_path=data --checkpoint_path=ckpts_rank_0/inceptionV4-train-rank0-50_1864.ckpt
## 测试精度 'Top1-Acc': 0.9562945973496432
![image](https://user-images.githubusercontent.com/67614464/142162794-13d221fc-bbbe-49fc-b33d-7ba29633ebdb.png)

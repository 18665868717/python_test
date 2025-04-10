import yaml

class test_Yaml_unity:
    @staticmethod
    def read_yaml(path,key):
        with open(path,'r',encoding="utf-8")as f:
            data=yaml.safe_load(f)
            print(data)
            data1=data[key]
            # print(data1)
            return list(data1.values())

    # print(a)
if __name__ == '__main__':
    test_Yaml_unity.read_yaml('data.yaml', 'login')
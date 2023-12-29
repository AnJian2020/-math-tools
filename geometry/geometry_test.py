import unittest


if __name__ == "__main__":
    # 加载测试用例
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir='./geometry', pattern='test_*.py')

    # 执行测试用例并输出结果
    runner = unittest.TextTestRunner()
    result = runner.run(tests)

    # 输出测试结果统计信息
    print('Total tests run:', result.testsRun)
    print('Number of failures:', len(result.failures))
    print('Number of errors:', len(result.errors))
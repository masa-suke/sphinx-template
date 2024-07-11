# -*- coding: utf-8 -*-
# %% [code]
import logging

logger = logging.getLogger(__name__)


class MyClass2:
    """サンプルクラス2
    
    :param arg1: コンストラクタ引数-arg1の説明
    :param arg2: コンストラクタ引数-arg2の説明
    """
    
    def __init__(self, arg1:int, arg2:int):
        logger.debug("MyClass2.__init__() called.")
    
    def my_method(self, arg1:int, arg2:int) -> float:
        """メソッド2の説明
        
        :param arg1: arg1の説明
        :param arg2: arg2の説明
        :return: 戻り値の説明
        """
        logger.debug("MyClass2.my_method() called.")
        res = arg1 + arg2
        return res


if __name__ == "__main__":
    import sys
    
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        stream=sys.stdout)
    obj = MyClass2(1, 2)
    res = obj.my_method(1, 2)
        
# %%
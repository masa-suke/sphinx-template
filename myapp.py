# -*- coding: utf-8 -*-
# %% [code]
import lib
import logging

logger = logging.getLogger(__name__)


def app_func(arg1:int, arg2:int) -> float:
    """アプリケーション関数の説明
    
    :param arg1: コンストラクタ引数-arg1の説明
    :param arg2: コンストラクタ引数-arg2の説明
    :return: 戻り値の説明
    """
    logger.debug("app_func() called.")
    return arg1 + arg2
    

def app_main(arg1:int, arg2:int):
    """アプリケーション関数の説明
    
    :param arg1: arg1の説明
    """
    logger.debug("app_main() called.")
    
    myobj1 = lib.MyClass1(arg1, arg2)
    myobj1.my_method(arg1, arg2)
    
    myobj2 = lib.MyClass2(arg1, arg2)
    myobj2.my_method(arg1, arg2)
    
    res = app_func(arg1, arg2)
    return res


if __name__ == "__main__":
    import sys
    
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        stream=sys.stdout)
    app_main(1, 2)
        
# %%
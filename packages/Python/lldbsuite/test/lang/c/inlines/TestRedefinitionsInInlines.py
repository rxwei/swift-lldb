from lldbsuite.test import lldbinline
from lldbsuite.test import decorators

<<<<<<< HEAD
lldbinline.MakeInlineTest(__file__, globals(), [decorators.expectedFailureAll(oslist=["windows"], bugnumber="llvm.org/pr27845"),
                                                decorators.expectedFailureAll(compiler="clang", compiler_version=["<", "3.5"], bugnumber="llvm.org/pr27845")])
=======
lldbinline.MakeInlineTest(__file__, globals(), [])
>>>>>>> origin/master

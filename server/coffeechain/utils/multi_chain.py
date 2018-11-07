import abc

from django.conf import settings

from coffeechain.common.constants import Chain


# noinspection PyPep8Naming
class chain_(object):
    """
    Class based decorator which adds a `chain` attribute, marking it as applying to a specific blockchain
    """

    def __init__(self, chain: Chain):
        self.chain = chain

    def __call__(self, func):
        """
        Only called ONCE, as part of the decoration process!
        Equivilant to:
            def foo():
                pass
            foo = for_chain(Chain.SAWTOOTH)(foo)
        """
        assert not hasattr(func, 'chain'), "Already decorated with .chain!"
        setattr(func, 'chain', self.chain)

        # just return the modified function, we don't need a proxy
        # function in this case, since ware aren't adding any pre/post logic
        return func


def get_for_chain(*args):
    """
    Returns whichever arg applies to the current chain, but inspecting the .chain attribute
    ----
    Does not currently check that all chains are represented.
    Throws an exception if chains are duplicated.
    """
    assert all(hasattr(f, 'chain') for f in args), "`chain` attr not found on one or more args"
    assert len(set(getattr(f, 'chain') for f in args)) == len(args), "Multiple functions define the same `.chain`"

    for obj in args:
        if getattr(obj, 'chain') == settings.CHAIN:
            return obj

    raise Exception("No object found for chain '%s'" % settings.Chain)


class MultiChainCallable(object, metaclass=abc.ABCMeta):
    """
    Returns a class that runs chain-specific functionality when call(),
    to be used like a class based function.  Needs renaming?
    """

    def __call__(self, *args, **kwargs):
        """
        Override the NEW method so we can call the class directly
        instead of actually instantiating it first, similar to a function
        """
        if settings.CHAIN == Chain.BIGCHAIN:
            return self.bigchain(*args, **kwargs)
        elif settings.CHAIN == Chain.SAWTOOTH:
            return self.sawtooth(*args, **kwargs)
        else:
            raise Exception("Unknown value for settings.CHAIN: %r" % settings.CHAIN)

    @abc.abstractmethod
    def bigchain(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def sawtooth(self, *args, **kwargs):
        pass


class MultiChain(metaclass=abc.ABCMeta):
    """
    Class that runs chain-specific code when the class is *instantiated*
    Instances should be treated like functions.

    -- if we can find a better way to this but keep it looking clean, i'm all for it!

    class MyView(APIView):
        def post(self, request):
            resp = self.DoChainLogic()
            ...

        class DoChainLogic(MultiChain):
            def bigchain(self, *args, **kwargs):
                return do_something()

            def sawtooth(self, *args, **kwargs):
                return do_something_else()
    """

    def __new__(cls, *args, **kwargs):
        """
        Override the NEW method so we can call the class directly.
        Does not return a class instances, it returns whatever bigchain() and sawtooth() functions return
        instead of actually instantiating it first, similar to a function
        """
        self = super().__new__(cls)  # internal instance, for calling the abstract functions
        if settings.CHAIN == Chain.BIGCHAIN:
            return self.bigchain(*args, **kwargs)
        elif settings.CHAIN == Chain.SAWTOOTH:
            return self.sawtooth(*args, **kwargs)
        else:
            raise Exception("Unknown value for settings.CHAIN: %r" % settings.CHAIN)

    @abc.abstractmethod
    def bigchain(self, *args, **kwargs):
        raise NotImplemented()

    @abc.abstractmethod
    def sawtooth(self, *args, **kwargs):
        raise NotImplemented()

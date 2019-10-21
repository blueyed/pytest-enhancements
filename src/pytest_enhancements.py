import _pytest
import _pytest.mark


class PatchedParameterSet(_pytest.mark.ParameterSet):
    @staticmethod
    def _parse_parametrize_parameters(argvalues, force_tuple):
        if not isinstance(argvalues, dict):
            return super().extract_from(argvalues, force_tuple)

        # Patch.
        return [
            PatchedParameterSet.extract_from(v, force_tuple=force_tuple)._replace(id=k)
            for k, v in argvalues.items()
        ]


_pytest.mark.ParameterSet = PatchedParameterSet

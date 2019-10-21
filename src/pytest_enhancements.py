import _pytest.mark


class ParameterSet(_pytest.mark.ParameterSet):
    @staticmethod
    def _parse_parametrize_parameters(argvalues, force_tuple):
        if not isinstance(argvalues, dict):
            return super(ParameterSet, ParameterSet)._parse_parametrize_parameters(
                argvalues, force_tuple
            )
        # Patch.
        extract_from = _pytest.mark.ParameterSet.extract_from
        return [
            extract_from(v, force_tuple=force_tuple)._replace(id=k)
            for k, v in argvalues.items()
        ]


_pytest.mark.ParameterSet = ParameterSet

def test_parametrize_vanilla(testdir):
    p1 = testdir.makepyfile(
        """
        import pytest

        @pytest.mark.parametrize('arg1,arg2', [
            (1, 2),
        ])
        def test_parametrize_dict(arg1, arg2):
            pass
        """
    )
    result = testdir.runpytest_subprocess(str(p1))
    assert result.ret == 0
    result.stdout.fnmatch_lines(["*= 1 passed in*"])


def test_parametrize_with_dict(testdir):
    p1 = testdir.makepyfile(
        """
        import pytest

        @pytest.mark.parametrize('arg1,arg2,expected_id', {
            "myid_12": [1, 2, "[myid_12]"],
            "replaced_id": pytest.param(3, 4, "[replaced_id]", id="myid_34"),
            "myid_56": pytest.param(5, 6, "[myid_56]"),
        })
        def test_parametrize_dict(request, arg1, arg2, expected_id):
            if expected_id is None:
                expected_id = "[%d-%d-None]" % (arg1, arg2)
            assert request.node.nodeid.endswith(expected_id)
        """
    )
    result = testdir.runpytest_subprocess(str(p1))
    assert result.ret == 0
    result.stdout.fnmatch_lines(["*= 3 passed in*"])


def test_parametrize_with_dict_single_string_arg(testdir):
    p1 = testdir.makepyfile(
        """
        import pytest

        @pytest.mark.parametrize('arg1', {
            "myid": "single_string_arg",
        })
        def test_parametrize_dict_single_arg(request, arg1):
            assert request.node.nodeid.endswith("[myid]")
        """
    )
    result = testdir.runpytest_subprocess(str(p1))
    assert result.ret == 0
    result.stdout.fnmatch_lines(["*= 1 passed in*"])

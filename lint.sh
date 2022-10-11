# TODO: add autopep8 here.
pep8_check(){
    local root="$1"
    local filename=""
    for f in 'ls $1'
    do
        filename = ${root}"/"${f}
        if [-d $filename]
        then
            pep8_check $filename
        elif [ "${filename##*.}" == "py"]
        then
            autopep8 --in-place $filename
        fi
    done
}
pep8_check .
# TODO: add autoflake here.
flake_check(){
    local root="$1"
    local filename=""
    for f in 'ls $1'
    do
        filename = ${root}"/"${f}
        if [-d $filename]
        then
            flake_check $filename
        elif [ "${filename##*.}" == "py"]
        then
            autoflake --in-place $filename
        fi
    done
}
flake_check .
# TODO: add isort here.
isort .

# TODO: add flake8 here.
flake8
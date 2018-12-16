#!/bin/bash
VERSION=patch
CUT_RELEASE=NO

while [ "$1" != "" ]; do
    case $1 in
        -v|--version)
            if [ -n "$2" ]; then
                VERSION=$2

                shift   # Past Argument
                shift   # Past Value

                continue
            else
                echo "ERROR: '-v|--version' requires a non-empty Option Argument."

                exit 1
            fi
        ;;
        --cut-release)
            CUT_RELEASE=YES

            shift   # past argument
        ;;
        --) # End of all options.
            shift

            break
        ;;
        -?*)
            echo "WARNING: Unknown Option (ignored): $1"
        ;;
        *)  # Default case: If no more options then break out of the loop.
            break
    esac
    shift
done

echo VERSION = "${VERSION}"

echo "========================================================================"
echo "Going to bump the Version."
echo "========================================================================"

bumpversion $VERSION --allow-dirty

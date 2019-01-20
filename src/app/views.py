import inspect

from django.shortcuts import render

from termcolor import colored


# -----------------------------------------------------------------------------
# --- HANDLERS
# -----------------------------------------------------------------------------
def handler400(request):
    """400 Handler."""
    print colored("***" * 27, "green")
    print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

    return render(request, "error-pages/400.html", status=404)


def handler403(request):
    """403 Handler."""
    print colored("***" * 27, "green")
    print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

    return render(request, "error-pages/403.html", status=404)


def handler404(request):
    """404 Handler."""
    print colored("***" * 27, "green")
    print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

    return render(request, "error-pages/404.html", status=404)


def handler500(request):
    """500 Handler."""
    print colored("***" * 27, "green")
    print colored("*** INSIDE `%s`" % inspect.stack()[0][3], "green")

    try:
        clear_cache.Command().handle()

        # ---------------------------------------------------------------------
        # --- Save the Log
        papertrail.log(
            event_type="500-exception",
            message="Cache cleared",
            data={
                "success":      True,
            },
            # timestamp=timezone.now(),
            targets={},
            )

    except Exception as e:
        print colored("###" * 27, "white", "on_red")
        print colored("### EXCEPTION @ `{module}`: {msg}".format(
            module=inspect.stack()[0][3],
            msg=str(e),
            ), "white", "on_red")

    return render(request, "error-pages/500.html", status=500)

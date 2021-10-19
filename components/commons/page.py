from flask import request, render_template


def render_page(context, slot, payload):  # pylint: disable=R0201,W0613
    """ Base template slot """
    chapter = request.args.get('chapter', '')
    module = request.args.get('module', '')
    page = request.args.get('page', '')
    try:
        if page:
            return render_template(f"{chapter.lower()}/{module.lower()}/{page.lower()}.html", active_chapter=chapter,
                                   config=payload)
        return render_template(f"{chapter.lower()}/{module.lower()}.html", active_chapter=chapter, config=payload)
    except:
        return render_template(f"common/empty.html", active_chapter=chapter, config=payload)


def render_test(context, slot, payload):  # pylint: disable=R0201,W0613
    """ Base template slot """
    chapter = request.args.get('chapter', '')
    module = request.args.get('module', '')
    try:
        if module:
            return render_template(f"{chapter.lower()}/{module.lower()}/create.html", active_chapter=chapter,
                                   config=payload)
        return render_template(f"{chapter.lower()}/create.html", active_chapter=chapter, config=payload)
    except:
        return render_template(f"common/empty.html", active_chapter=chapter, config=payload)


def render_run_test(context, slot, payload):  # pylint: disable=R0201,W0613
    """ Base template slot """
    chapter = request.args.get('chapter', '')
    module = request.args.get('module', '')
    try:
        if module:
            return render_template(f"{chapter.lower()}/{module.lower()}/runtest.html", active_chapter=chapter,
                                   config=payload)
        return render_template(f"{chapter.lower()}/runtest.html", active_chapter=chapter, config=payload)
    except:
        return render_template(f"common/empty.html", active_chapter=chapter, config=payload)


def reporting_config(context, slot, payload):
    return render_template(f"common/reporting-config.html", config=payload)


def params_table(context, slot, payload):
    return render_template(f"common/params_table.html", config=payload)


def locations(context, slot, payload):
    return render_template(f"common/locations.html", config=payload)


def source_card(context, slot, payload):
    return render_template(f"common/source_card.html", config=payload)


def render_tests_result_page(context, slot, payload):
    chapter = request.args.get('chapter', '')
    module = request.args.get('module', '')
    test_data = context.rpc_manager.timeout(5).security_results_or_404(request.args.get('result_test_id'))
    payload['test_data'] = test_data
    try:
        return render_template(f"{chapter.lower()}/{module.lower()}/test_running_result.html", active_chapter=chapter, config=payload)
    except:
        return render_template(f"common/empty.html", active_chapter=chapter, config=payload)

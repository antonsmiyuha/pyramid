<%inherit file="layout.mako" />

<div class="panel panel-default">
    <div class="panel-heading">
        <h1>Feedback Form</h1>

    </div>
    <div class="panel-body">
        <form method="post" id="feedback-form" action="/feedback/save">
            <div class="form-group row">
                <label for="name" class="col-2 col-form-label">Name</label>
                <div class="col-10">
                    <input class="form-control" id="name" type="text" name="name" value="${h.get_data(data, 'name')}">
                </div>
            </div>
            <div class="form-group row">
                <label for="email" class="col-2 col-form-label">Email</label>
                <div class="col-10">
                    <input class="form-control" id="email" type="email" name="email"
                           value="${h.get_data(data, 'email')}">
                </div>
            </div>
            <div class="form-group row">
                <label for="tel" class="col-2 col-form-label">Phone</label>
                <div class="col-10">
                    <input class="form-control" id="tel" type="tel" name="phone" value="${h.get_data(data, 'phone')}">
                </div>
            </div>
            <div class="form-group row">
                <label for="subject" class="col-2 col-form-label">Subject</label>
                <div class="col-10">
                    <select class="form-control" id="subject" name="subject">
                        %for subject in h.get_subjects():
                            <option ${h.selected(h.get_data(data, 'subject'), subject)}
                                    value="${subject}">${subject}</option>
                        %endfor
                        <option value="other">Other Subject</option>
                    </select>
                </div>
            </div>
            <div id="other-subject-block" class="form-group row" hidden>
                <label for="other-subject" class="col-2 col-form-label">Other Subject</label>
                <div class="col-10">
                    <input class="form-control" id="other-subject" type="text" name="other_subject" disabled="disabled"
                           value="${h.get_data(data, 'other_subject')}">
                </div>
            </div>
            <div class="form-group row">
                <label for="message" class="col-2 col-form-label">Message</label>
                <div class="col-10">
                    <textarea class="form-control" id="message" rows="10"
                              name="message">${h.get_data(data, 'message')}</textarea>
                </div>
            </div>
            <div class="form-group row">
                <div class="col-12">
                    <div class="g-recaptcha" data-sitekey="6LeXUhsUAAAAAKTgGqG4Q6gewg88d3FmqMQ7IeJC"></div>
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</div>

<script>
    document.addEventListener("DOMContentLoaded", function () {
        var feedback = new Feedback('feedback-form');
    });
</script>


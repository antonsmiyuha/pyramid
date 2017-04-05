<%inherit file="layout.mako" />

<div class="panel panel-default">
    <div class="panel-heading">
        <h1>Feedback Form</h1>
    </div>
    <div class="panel-body">
        <form method="post" id="feedback-form" action="/update">
            <input type="hidden" value="${data.id}" name="id">
            <div class="form-group row">
                <label for="name" class="col-2 col-form-label">Name</label>
                <div class="col-10">
                    <input class="form-control" id="name" type="text" name="name" value="${data.name}">
                </div>
            </div>
            <div class="form-group row">
                <label for="email" class="col-2 col-form-label">Email</label>
                <div class="col-10">
                    <input class="form-control" id="email" type="email" name="email"
                           value="${data.email}">
                </div>
            </div>
            <div class="form-group row">
                <label for="tel" class="col-2 col-form-label">Phone</label>
                <div class="col-10">
                    <input class="form-control" id="tel" type="tel" name="phone" value="${data.phone}">
                </div>
            </div>
            <div class="form-group row">
                <label for="subject" class="col-2 col-form-label">Subject</label>
                <div class="col-10">
                    <input class="form-control" id="subject" type="text" name="subject"
                           value="${data.subject}">
                </div>
            </div>
            <div class="form-group row">
                <label for="status" class="col-2 col-form-label">Status</label>
                <div class="col-10">
                    <select class="form-control" id="status" name="status">
                        %for status in h.get_statuses():
                            <option ${h.selected(data.status, status)} value="${status}">${status}</option>
                        %endfor
                    </select>
                </div>
            </div>
            <div class="form-group row">
                <label for="message" class="col-2 col-form-label">Message</label>
                <div class="col-10">
                    <textarea class="form-control" id="message" rows="10"
                              name="message">${data.message}</textarea>
                </div>
            </div>
            <button type="submit" style="cursor:pointer;" class="btn btn-success">Submit</button>
            <a href="${request.route_url('delete', _query={'id': data.id})}"
               class="btn btn-danger">Delete</a>
        </form>
    </div>
</div>


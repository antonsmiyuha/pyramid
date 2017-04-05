<%inherit file="layout.mako" />
<div class="col-lg-12">
    <h2>Feedback</h2>
    <table class="table table-striped">
        <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Subject</th>
            <th>Message</th>
            <th>Created</th>
            <th>Updated</th>
            <th>Customer IP</th>
            <th>Status</th>
            <th></th>
            <th></th>
        </tr>
        </thead>
        <tbody>
            % for item in collection:
                <tr>
                    <td>${ item.name }</td>
                    <td>${ item.email }</td>
                    <td>${ item.phone }</td>
                    <td>${ item.subject }</td>
                    <td>${ item.message }</td>
                    <td>${ item.created_at }</td>
                    <td>${ item.updated_at }</td>
                    <td>${ item.customer_ip }</td>
                    <td>${ item.status }</td>
                    <td><a class="btn btn-success" href="${ request.route_url('edit', _query={'id': item.id})}">Edit</a>
                    </td>
                    <td>
                        <a href="${request.route_url('delete', _query={'id': item.id})}"
                           class="btn btn-danger">Delete</a>
                    </td>
                </tr>
            % endfor
        </tbody>
    </table>
</div>
<ul class="pagination">
    %for page in range(1, pages):
        <li class="page-item"><a class="page-link"
                                 href="${ request.route_url('list', _query={'page': page}) }">${ page }</a></li>
    %endfor
</ul>

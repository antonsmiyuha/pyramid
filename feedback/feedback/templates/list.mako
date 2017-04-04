<%inherit file="layout.mako" />
<div class="container">
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
                </tr>
            % endfor

        </tbody>
    </table>
</div>
<ul class="pagination">
    ##         {% for page in range(1 - pages) %}
##             <li class="page-item"><a class="page-link"
##                                      href="{{ request.route_url('list', _query={'page': page}) }}">{{ page }}</a></li>
##         {% endfor %}
    </ul>
